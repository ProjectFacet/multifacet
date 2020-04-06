from django.db import models
from django.db.models import Q

from editorial.models import SimpleImage, SimpleDocument, SimpleAudio, SimpleVideo
from editorial.models import Project, Story
from base.models import Participant
from entity.models import NewsOrganization
from . import User, Organization, Project, Story


class Event(models.Model):
    """An Event.

    An event is an action item assigned to a Project, Story or Event.
    An event has an assigned team of participants.

    Events are unique in that they have:
    - anchor_profile field, because Notes and Discussion can be connected to them
    - anchor field because they are connected to Project, Story, Event
    """

    anchor_profile = models.OneToOneField(Anchor, on_delete=models.CASCADE)

    participant_owner = models.OneToOneField(
        Participant,
        help_text = 'Participant who created/owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    # object this is bound to
    anchor = models.OneToOneField(
        Anchor,
        null=True,
        on_delete=models.SET_NULL,
        help_text='The anchor object',
    )

    name = models.TextField(
        help_text='Name of the event.'
    )

    text = models.TextField(
        help_text='Description of the event.',
        blank=True,
    )

    # Choices for event type:
    # Hosting: An event that is managed by an organization.
    # Ex - Live studio taping open to the public
    # Reporting: An external event that is being covered for a story.
    # Ex - Press conference at the police department
    # Administrative: An internal event such as a team meeting or conference call
    HOSTING = 'Hosting'
    REPORTING = 'Reporting'
    ADMINISTRATIVE = 'Administrative'
    OTHER = 'Other'
    EVENT_TYPE_CHOICES = (
        (HOSTING, 'Hosting'),
        (REPORTING, 'Reporting'),
        (ADMINISTRATIVE, 'Administrative'),
        (OTHER, 'Other'),
    )

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPE_CHOICES,
        help_text='Kind of event.'
    )

    team = models.ManyToManyField(
        # There can be multiple users assigned to an event.
        User,
        related_name='eventteam',
        help_text='The users assigned to an event.',
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time event is created.',
        blank=True,
    )

    event_date = models.DateTimeField(
        help_text='Date and time of the event.',
        blank=True,
    )

    venue = models.TextField(
        help_text = 'The location of the event.',
        blank=True,
    )

    # notes
    notes = models.ManyToManyField('Note', blank=True)

    # simple assets
    simple_image_assets = models.ManyToManyField(SimpleImage, blank=True)
    simple_document_assets = models.ManyToManyField(SimpleDocument, blank=True)
    simple_audio_assets = models.ManyToManyField(SimpleAudio, blank=True)
    simple_video_assets = models.ManyToManyField(SimpleVideo, blank=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.id})


    def get_event_team_vocab(self):
        """Return queryset with org users and users from collaborating orgs for the parent
        of the event. Used in selecting assigned users for event team.
        """

        from . import User
        # TODO future: add contractors

        if self.evt_organization:
            parent = self.evt_organization
        elif self.project:
            parent = self.project
        elif self.story:
            parent = self.story

        if parent.type == "project" or "story":
            collaborators = parent.collaborate_with.all()
            owner = parent.organization
            event_vocab = User.objects.filter(Q(Q(organization=self.organization) | Q(organization__in=collaborators) | Q(organization=owner)))
        else:
            event_vocab = self.organization.get_org_users()

        return event_vocab


    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Event"

    @property
    def description(self):
        return self.text

    # def clean(self):
    #     """Enforce that there is one relationship."""
    #
    #     super(Event, self).clean()
    #
    #     count = (
    #         (1 if self.evt_organization else 0) +
    #         (1 if self.project else 0) +
    #         (1 if self.story else 0)
    #     )
    #
    #     if count != 1:
    #         raise ValidationError("Events can only relate to one thing.")

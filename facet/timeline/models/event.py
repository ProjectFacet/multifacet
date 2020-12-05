from django.db import models
from django.db.models import Q

from base.models import Participant, Anchor, EntityOwner
from note.models import Note
from internalasset.models import InternalImage, InternalDocument, InternalAudio, InternalVideo


class Event(models.Model):
    """An Event.

    An event is an action item assigned to a Project, Story or Event.
    An event has an assigned team of participants.

    Events are unique in that they have:
    - anchor_profile field, because Notes and Discussion can be connected to them
    - anchor field because they are connected to Project, Story, Event
    """

    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)

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
        related_name='event_anchor',
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
        # There can be multiple participants assigned to an event.
        Participant,
        related_name='event_team',
        help_text='The participants assigned to an event.',
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
    notes = models.ManyToManyField(Note, blank=True)

    # internal assets
    internal_images = models.ManyToManyField(InternalImage, blank=True)
    internal_documents = models.ManyToManyField(InternalDocument, blank=True)
    internal_audio = models.ManyToManyField(InternalAudio, blank=True)
    internal_videos = models.ManyToManyField(InternalVideo, blank=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = "Events"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.id})

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Event"

    @property
    def description(self):
        return self.text

    # def get_event_team_vocab(self):
    #     """Return queryset with org participants and participants from collaborating orgs for the parent
    #     of the event. Used in selecting assigned participants for event team.
    #     """
    #
    #     from . import Participant
    #     # TODO future: add contractors
    #
    #     if self.evt_organization:
    #         parent = self.evt_organization
    #     elif self.project:
    #         parent = self.project
    #     elif self.story:
    #         parent = self.story
    #
    #     if parent.type == "project" or "story":
    #         collaborators = parent.partner_with.all()
    #         owner = parent.organization
    #         event_vocab = Participant.objects.filter(Q(Q(organization=self.organization) | Q(organization__in=collaborators) | Q(organization=owner)))
    #     else:
    #         event_vocab = self.organization.get_org_participants()
    #
    #     return event_vocab

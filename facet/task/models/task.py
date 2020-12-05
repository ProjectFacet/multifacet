from django.db import models
from django.db.models import Q

from base.models import Participant, Anchor, EntityOwner
from internalasset.models import InternalImage, InternalDocument, InternalAudio, InternalVideo
from note.models import Note

#-----------------------------------------------------------------------#
#  TASK
#-----------------------------------------------------------------------#

class Task(models.Model):
    """A Task.

    A task is an action item assigned to a Project, Story or Event.
    A task has an assigned team of participants.

    Tasks are unique in that they have:
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
        related_name='task_anchor',
        null=True,
        on_delete=models.SET_NULL,
        help_text='The anchor object',
    )

    name = models.TextField(
        help_text='Name of the task.'
    )

    text = models.TextField(
        help_text='Content of the task.',
        blank=True,
    )

    team = models.ManyToManyField(
        # There can be multiple participants listed as assigned to the task.
        Participant,
        related_name='task_team',
        help_text='The participants assigned to the task.',
        blank=True,
    )

    # Choices for Task status.
    IDENTIFIED = 'Identified'
    IN_PROGRESS = 'In Progress'
    COMPLETE = 'Complete'
    TASK_STATUS_CHOICES = (
        (IDENTIFIED, 'Identified'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETE, 'Complete'),
    )

    status = models.CharField(
        max_length=50,
        choices=TASK_STATUS_CHOICES,
        help_text='Task status.'
    )

    important = models.BooleanField(
        default=False,
        help_text='Whether a task is important.'
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time task is created.',
        blank=True,
    )

    due_date = models.DateTimeField(
        help_text='Date and time task is to be completed.',
        blank=True,
    )

    inprogress_date = models.DateTimeField(
        help_text='Date and time task status is changed to in progress.',
        blank=True,
        null=True,
    )

    completion_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time task status is changed to complete.',
        blank=True,
        null=True,
    )

    # notes
    notes = models.ManyToManyField(Note, blank=True)

    # internal assets
    internal_images = models.ManyToManyField(InternalImage, blank=True)
    internal_documents = models.ManyToManyField(InternalDocument, blank=True)
    internal_audio = models.ManyToManyField(InternalAudio, blank=True)
    internal_videos = models.ManyToManyField(InternalVideo, blank=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = "Tasks"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.id})

    def get_task_assignment_vocab(self):
        """Return queryset with org participants and participants from collaborating orgs for the parent
        of the task. Used in selecting assigned participants for a task.
        """

        from . import Participant

        if self.project:
            parent = self.project
        elif self.story:
            parent = self.story
        else:
            parent = self.event

        if parent.type == "project" or "story":
            collaborators = parent.partner_with.all()
            owner = parent.organization
            task_vocab = Participant.objects.filter(Q(Q(organization=self.organization) | Q(organization__in=collaborators) | Q(organization=owner)))
        else:
            task_vocab = self.organization.get_org_participants()

        return task_vocab

    @property
    def search_title(self):
        return self.name

    @property
    def description(self):
        return self.text.encode('utf-8')

    @property
    def type(self):
        return "Task"

    # def clean(self):
    #     """Enforce that there is one relationship."""
    #
    #     super(Task, self).clean()
    #
    #     count = (
    #         (1 if self.project else 0) +
    #         (1 if self.story else 0) +
    #         (1 if self.event else 0)
    #     )
    #
    #     if count != 1:
    #         raise ValidationError("Tasks can only relate to one thing.")

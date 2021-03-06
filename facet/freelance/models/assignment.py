from django.db import models

from base.models import Anchor
from participant.models import FreelanceJournalist
from participant.models import FreelanceManager
from entity.models import NewsOrganization
from editorial.models import Project, Story, Item
from .call import Call
from .pitch import Pitch
from internalasset.models import InternalImage, InternalDocument, InternalAudio, InternalVideo
from note.models import Note

class Assignment(models.Model):
    """The details of an assignment to a freelancer from an organization."""

    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)

    freelancer = models.ForeignKey(
        FreelanceJournalist,
        null=True,
        on_delete = models.CASCADE,
    )

    editor = models.ForeignKey(
        FreelanceManager,
        null=True,
        help_text='Editor responsible for this assignment.',
        on_delete = models.CASCADE,
    )

    organization = models.ForeignKey(
        NewsOrganization,
        help_text='Organization that owns this assignment.',
        on_delete = models.CASCADE,
    )

    name = models.TextField(
        help_text='Name of the assignment.',
    )

    text = models.TextField(
        help_text='Details of the assignment.',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Day assignment was created.',
        blank=True,
    )

    # An assignment can be connected to a story, giving the freelancer access
    # to all details of the story.
    # OR an assignment can be connected to a specific item, giving the freelancer
    # access to only that item of the story.
    # The story or item could be an existing one or newly created through the assignment.
    project = models.ForeignKey(
        Project,
        on_delete = models.SET_NULL,
        help_text='Which project is this assignment related to?',
        blank=True,
        null=True,
    )

    story = models.ForeignKey(
        Story,
        on_delete = models.SET_NULL,
        help_text='Which story is this assignment related to?',
        blank=True,
        null=True,
    )

    item = models.ForeignKey(
        Item,
        on_delete = models.SET_NULL,
        help_text='Which item is this assignment related to?',
        blank=True,
        null=True,
    )

    call = models.ForeignKey(
        Call,
        on_delete = models.SET_NULL,
        help_text='If this assignment is related to a call, which one?',
        blank=True,
        null=True,
    )

    pitch = models.ForeignKey(
        Pitch,
        on_delete = models.SET_NULL,
        help_text='If this assignment is related to a pitch, which one?',
        blank=True,
        null=True,
    )

    complete = models.BooleanField(
        default=False,
        help_text='Is the assignment complete?',
    )

    rate = models.CharField(
        max_length=100,
        help_text='Rate at which the assignment is being completed.',
    )

    invoiced = models.BooleanField(
        default=False,
        help_text='An invoice has been submitted for this assignment.',
    )

    paid = models.BooleanField(
        default=False,
        help_text='Payment has been remitted for this assignment.',
    )

    # notes
    notes = models.ManyToManyField(Note, blank=True)

    # internal assets
    internal_image_assets = models.ManyToManyField(InternalImage, blank=True)
    internal_document_assets = models.ManyToManyField(InternalDocument, blank=True)
    internal_audio_assets = models.ManyToManyField(InternalAudio, blank=True)
    internal_video_assets = models.ManyToManyField(InternalVideo, blank=True)

    class Meta:
        verbose_name = 'Freelance Assignment'
        verbose_name_plural = 'Freelance Assignments'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('assignment_detail', kwargs={'pk': self.id})

    @property
    def search_title(self):
        return self.name

    @property
    def description(self):
        return self.text

    @property
    def type(self):
        return "Assignment"

from django.db import models

from base.models import Anchor
from participant.models import FreelanceJournalist
from participant.models import FreelanceManager
from .call import Call
from internalasset.models import InternalImage, InternalDocument, InternalAudio, InternalVideo


class Pitch(models.Model):
    """ Pitches for content from a freelancer to a news organization."""

    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)

    freelancer = models.ForeignKey(
        FreelanceJournalist,
        null=True,
        on_delete = models.CASCADE,
    )

    recipient = models.ForeignKey(
        FreelanceManager,
        help_text='Freelance Manager being pitched.',
        on_delete = models.SET_NULL,
        blank=True,
        null=True,
    )

    call = models.ForeignKey(
        Call,
        help_text='Call if pitch is in response to a call.',
        on_delete = models.SET_NULL,
        blank=True,
        null=True,
    )

    name = models.TextField(
        help_text='Title of the pitch.',
    )

    text = models.TextField(
        help_text='Text of the pitch.',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Day pitch was created.',
        blank=True,
    )

    DRAFT = 'Draft'
    PITCHED = 'Pitched'
    ACCEPTED = 'Accepted'
    COMPLETE = 'Complete'

    PITCH_STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PITCHED, 'Pitched'),
        (ACCEPTED, 'Accepted'),
        (COMPLETE, 'Complete'),
    )

    #status is determined by contributor that owns the pitch
    status = models.CharField(
        max_length=25,
        choices=PITCH_STATUS_CHOICES,
        help_text='Pitch status choice.'
    )

    exclusive = models.BooleanField(
        default=False,
        help_text='Is this pitch for an assignment exclusive to the recipient?',
    )

    # internal assets
    internal_image_assets = models.ManyToManyField(InternalImage, blank=True)
    internal_document_assets = models.ManyToManyField(InternalDocument, blank=True)
    internal_audio_assets = models.ManyToManyField(InternalAudio, blank=True)
    internal_video_assets = models.ManyToManyField(InternalVideo, blank=True)

    tags = models.ManyToManyField('editorial.Tag', blank=True)

    class Meta:
        verbose_name = 'Freelance Pitch'
        verbose_name_plural = 'Freelance Pitches'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('pitch_edit', kwargs={'pk': self.id})

    @property
    def search_title(self):
        return self.name

    @property
    def description(self):
        return self.text

    @property
    def type(self):
        return "Pitch"

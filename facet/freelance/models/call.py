from django.db import models
from django.contrib.postgres.fields import ArrayField

from participant.models import FreelanceManager
from entity.models import NewsOrganization
from internalasset.models import InternalImage, InternalDocument, InternalAudio, InternalVideo
from editorial.models import Tag


class Call(models.Model):
    """Calls are requests from editors/organizations for pitches.

    They contain details for what pitches they are requesting.
    """

    owner = models.ForeignKey(
        FreelanceManager,
        null=True,
        help_text='Freelance Manager that owns this call.',
        on_delete = models.CASCADE,
    )

    organization = models.ForeignKey(
        NewsOrganization,
        help_text='NewsOrganization that is making this call.',
        on_delete = models.CASCADE,
    )

    name = models.CharField(
        max_length=50,
        help_text='Title of the call.',
    )

    text = models.TextField(
        help_text='Text of the call.',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Day/Time call was created.',
        blank=True,
    )

    # optional expiration date for call
    # at this point is_active will set to false automatically
    expiration_date = models.DateTimeField(
        help_text='Day/Time call ends.',
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
        help_text='Is this call active?'
    )

    urgent = models.BooleanField(
        default=False,
        help_text='The urgency of the call'
    )

    timeframe = models.CharField(
        max_length=100,
        help_text='The timeframe for response.',
        blank=True,
        null=True,
    )

    DRAFT = 'Draft'
    ACTIVE = 'Active'
    COMPLETE = 'Complete'

    CALL_STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (ACTIVE, 'Active'),
        (COMPLETE, 'Complete'),
    )

    # internal draft management. Only published calls are visible
    # to contractors.
    # status is determined by user that owns the call.
    status = models.CharField(
        max_length=25,
        choices=CALL_STATUS_CHOICES,
        help_text='Pitch status choice.'
    )

    # internal assets
    internal_images = models.ManyToManyField(InternalImage, blank=True)
    internal_documents = models.ManyToManyField(InternalDocument, blank=True)
    internal_audio = models.ManyToManyField(InternalAudio, blank=True)
    internal_videos = models.ManyToManyField(InternalVideo, blank=True)

    tags = models.ManyToManyField('editorial.Tag', blank=True)

    class Meta:
        verbose_name = 'Call for Pitch'
        verbose_name_plural = 'Calls for Pitch'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('call_detail', kwargs={'pk': self.id})

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Call for Pitch"

    @property
    def description(self):
        return self.text

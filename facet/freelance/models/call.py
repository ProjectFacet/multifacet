from django.db import models
from django.contrib.postgres.fields import ArrayField

from .journalist_freelancemanager import FreelanceManager
from entity.models import NewsOrganization
# from editorial.models import SimpleImage, SimpleDocument, SimpleAudio, SimpleVideo, Tag


class Call(models.Model):
    """Calls are requests from editors/organizations for pitches.

    They contain details for what pitches they are requesting.
    """

    owner = models.ForeignKey(
        FreelanceManager,
        help_text='Freelance Manager that owns this call.',
        on_delete = models.CASCADE,
    )

    organization = models.ForeignKey(
        NewsOrganization,
        help_text='Organization that is making this call.',
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
        help_text='Is this call urgent?'
    )

    timeframe = models.CharField(
        max_length=100,
        help_text='What is the timeframe for responses?',
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

    # simple assets
    simple_image_assets = models.ManyToManyField('editorial.SimpleImage', blank=True)
    simple_document_assets = models.ManyToManyField('editorial.SimpleDocument', blank=True)
    simple_audio_assets = models.ManyToManyField('editorial.SimpleAudio', blank=True)
    simple_video_assets = models.ManyToManyField('editorial.SimpleVideo', blank=True)

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

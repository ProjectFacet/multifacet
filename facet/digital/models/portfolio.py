from django.db import models

from base.models import Participant
from internalasset.models import InternalImage, InternalDocument, InternalAudio, InternalVideo


class PortfolioEntry(models.Model):
    """ Portfolio entry."""

    participant_owner = models.ForeignKey(
        Participant,
        help_text = 'Participant who owns the portfolio entry.',
        null = True,
        on_delete = models.SET_NULL,
    )

    name = models.CharField(
        help_text='Title of the portfolio entry',
        max_length=500,
    )

    description = models.TextField(
        help_text='Description of the portfolio entry.',
        blank=True,
    )

    link = models.URLField(
        max_length=500,
        help_text='Link to portfolio item.',
        blank=True,
        null=True,
    )

    date = models.DateTimeField(
        help_text='The publish date of the portfolio entry.',
        blank=True,
    )

    internal_images = models.ManyToManyField('internalasset.InternalImage', blank=True)
    internal_documents = models.ManyToManyField('internalasset.InternalDocument', blank=True)
    internal_audio = models.ManyToManyField('internalasset.InternalAudio', blank=True)
    internal_videos = models.ManyToManyField('internalasset.InternalVideo', blank=True)

    public = models.BooleanField(
        default=True,
        help_text='whether portfolio entry is shown on public profile.',
    )

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('portfolio_entry', kwargs={'pk': self.id})

    @property
    def search_title(self):
        return self.name

    @property
    def description(self):
        return self.description

    @property
    def type(self):
        return "Portfolio Entry"

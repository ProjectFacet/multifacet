from django.db import models

from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# from internal_history.models import HistoricalRecords
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from .partner import Partner
# from digital.models import PortfolioEntry

class Participant(AbstractUser):
    """Participant.

    The basic profile of a participant on the platform.
    """

    # for inclusion in collaborations
    partner_profile = models.OneToOneField(Partner, null=True, on_delete=models.SET_NULL)
    # notes
    notes = models.ManyToManyField('note.Note', blank=True)
    # portfolio
    portfolio = models.ManyToManyField('digital.PortfolioEntry', blank=True)

    connections = models.ManyToManyField(
        'self',
        blank=True,
        help_text='Participants that are connections.',
    )

    display_name = models.CharField(
        max_length=100,
        help_text='Shorter version of name used to identify participant to other participants.',
        blank=True,
    )

    credit_name = models.CharField(
        max_length=75,
        help_text='Full name of participant as listed as a public credit on content.',
        blank=True,
    )

    name_pronunciation = models.TextField(
        help_text='Instruction on the proper pronunciation of participant name.',
        blank=True,
    )

    pronoun = models.CharField(
        max_length=50,
        help_text='Participants preferred pronouns.',
        blank=True,
    )

    title = models.CharField(
        max_length=100,
        help_text='Professional title.',
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    biography = models.TextField(
        help_text="Short bio.",
        blank=True,
    )

    city = models.CharField(
        max_length=255,
        blank=True,
    )

    postal_code = models.CharField(
        max_length=15,
        blank=True,
    )

    expertise = ArrayField(
        models.CharField(max_length=255),
        default=list,
        help_text='Array of participant skills and beats to filter/search by.',
        blank=True,
    )

    photo = models.ImageField(
        upload_to='participants',
        blank=True,
    )

    display_photo = ImageSpecField(
        source='photo',
        processors=[SmartResize(500, 500)],
        format='JPEG',
    )


    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        ordering = ['credit_name']


    @property
    def initials(self):
        "Return's participant's initials based on their credit_name."
        return ''.join( [ letter[0] for letter in self.credit_name.split() ] )


    def get_partner_vocab(self):
        """Retrieve appropriate partners for the participant."""

        if self.staffjournalist:
            partners = self.staffjournalist.get_partner_vocab()
            return partners

        if self.unaffiliatedstaffjournalist:
            partners = self.unaffiliatedstaffjournalist.get_partner_vocab()
            return partners

        if self.freelancejournalist:
            partners = self.freelancejournalist.get_partner_vocab()
            return partners


    def get_image_library(self):
        """Retrieve appropriate image library for a participant."""

        if self.staffjournalist:
            return NewsOrganization.get_image_library(self.staffjournalist.newsorganization)
        else:
            return ImageAsset.objects.filter(participant_owner=self)
        # FIXME account for visibility of library to partner

    def get_document_library(self):
        """Retrieve appropriate document library for a participant."""

        if self.staffjournalist:
            return NewsOrganization.get_document_library(self.staffjournalist.newsorganization)
        else:
            return DocumentAsset.objects.filter(participant_owner=self)
        # FIXME account for visibility of library to partner

    def get_audio_library(self):
        """Retrieve appropriate audio library for a participant."""

        if self.staffjournalist:
            return NewsOrganization.get_audio_library(self.staffjournalist.newsorganization)
        else:
            return AudioAsset.objects.filter(participant_owner=self)
        # FIXME account for visibility of library to partner

    def get_video_library(self):
        """Retrieve appropriate video library for a participant."""

        if self.staffjournalist:
            return NewsOrganization.get_video_library(self.staffjournalist.newsorganization)
        else:
            return VideoAsset.objects.filter(participant_owner=self)
        # FIXME account for visibility of library to partner

    def get_copied_content(self):
        """Returns queryset of content picked up from a partner."""

        from . import StoryCopyDetail
        from . import Story

        copyrecords = StoryCopyDetail.objects.filter(partner=self.partner_profile)
        copied_content = [record.original_story for record in copyrecords]

        return copied_content

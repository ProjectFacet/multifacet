from django.db import models

from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# from simple_history.models import HistoricalRecords
# from imagekit.models import ImageSpecField
# from pilkit.processors import SmartResize

from .partner import Partner


class Participant(AbstractUser):
    """Participant.

    The basic profile of a participant on the platform.
    """

    # for inclusion in collaborations
    partner_profile = models.OneToOneField(Partner, null=True, on_delete=models.SET_NULL)
    # notes
    notes = models.ManyToManyField('note.Note', blank=True)

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

    # FIXME Pilkit install
    # photo = models.ImageField(
    #     upload_to='participants',
    #     blank=True,
    # )
    #
    # display_photo = ImageSpecField(
    #     source='photo',
    #     processors=[SmartResize(500, 500)],
    #     format='JPEG',
    # )


    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        ordering = ['credit_name']

from django.db import models

from base.models import Participant, Anchor

class Correction(models.Model):
    """Correction issued for story or item.

    A correction contains information required to address
    an error.
    """

    corrected_content = models.OneToOneField(
        Anchor,
        on_delete=models.CASCADE,
        related_name='correction_anchor_object',
        help_text='The anchor object',
    )

    text = models.TextField(
        help_text='Details regarding the correction.',
        blank=True,
    )

    contact = models.ForeignKey(
        Participant,
        help_text = 'For more information, contact:',
        null = True,
        on_delete = models.SET_NULL,
    )

    # severity: based on impact of correction
    # Choices for correction severity.
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'

    CORRECTION_PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    )

    priority = models.CharField(
        max_length=25,
        choices=CORRECTION_PRIORITY_CHOICES,
        help_text='Correction urgency.',
        default='LOW',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date time correction was created.',
    )

    class Meta:
        verbose_name='Correction'
        verbose_name_plural='Corrections'
        ordering = ['-creation_date']

    def __str__(self):
        return "{ priority } correction for { type } { name }".format(
            priority = priority,
            type = self.anchor.type,
            name = self.anchor.name,
        )

    # def get_absolute_url(self):
    #     return reverse('item_edit', kwargs={'pk': self.id, 'story': self.story_id})

    @property
    def type(self):
        return "Correction"

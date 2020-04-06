from django.db import models


class Update(models.Model):
    """Update issued for story or item.

    An update contains information regarding changes or
    additional information regarding a specific piece of content.

    Ex. A story about an event that happened.
    An update may be used to distribute new comment from someone involved.

    """

    updated_content = models.OneToOneField(
        Anchor,
        on_delete=models.CASCADE,
        related_name='anchor_object',
        help_text='The anchor object',
    )

    text = models.TextField(
        help_text='Details regarding the update.',
        blank=True,
    )

    contact = models.ForeignKey(
        Participant,
        help_text = 'For more information, contact:',
        null = True,
        on_delete = models.SET_NULL,
    )

    # Choices for update importance.
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'

    UPDATE_PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    )

    priority = models.CharField(
        max_length=25,
        choices=UPDATE_PRIORITY_CHOICES,
        help_text='Update urgency.',
        default='LOW',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date time update was issued.',
    )

    class Meta:
        verbose_name='Update'
        verbose_name_plural='Update'
        ordering = ['-creation_date']

    def __str__(self):
        return "{priority} update for {anchor.type} { anchor.name }".format(
            priority = priority,
            type = self.anchor.type,
            name = self.anchor.name,
        )

    # def get_absolute_url(self):
    #     return reverse('item_edit', kwargs={'pk': self.id, 'story': self.story_id})

    @property
    def type(self):
        return "Update"

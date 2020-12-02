from django.db import models

from base.models import Anchor


class Website(models.Model):
    """Link to a website."""

    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)

    url = models.URLField(
        max_length=500,
        help_text='Link to website.',
        blank=True,
        null=True,
    )

    description = models.CharField(
        max_length=500,
        help_text='Short description of web link.',
        blank=True,
    )

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = "URLs"
        ordering = ['anchor_profile']

    def __str__(self):
        return "{{ anchor type }} {{ anchor }} url".format(
            anchor = self.anchor_profile.anchor_name,
            anchor_type=self.anchor_profile.anchor_type,
        )

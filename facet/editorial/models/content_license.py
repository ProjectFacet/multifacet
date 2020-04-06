from django.db import models

from base.models import EntityOwner


class ContentLicense(models.Model):
    """Content License for items.

    Items can have a related content license. The data for this model
    includes the 7 established variations of the Creative Commons license;
    these have a blank entity_owner field.

    Organizations can also create their own content licenses/reuse terms and
    upload documents for the custom license.
    """

    entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    sitewide = models.BooleanField(
        help_text = 'If no ownership entity, True.',
        default=False,
    )

    custom = models.BooleanField(
        help_text = 'If created by entity or participant, True. If creative commons, False.',
        default=False,
    )

    name = models.TextField(
        help_text='Name for the license.',
    )

    terms = models.TextField(
        help_text='Content of the terms.',
        blank=True,
    )

    upload = models.FileField(
        upload_to="license/%Y/%m/%d/",
        null=True,
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Content License'
        verbose_name_plural = 'Content Licenses'
        ordering = ['name']

    def __str__(self):
        return self.name

from django.db import models

from base.models import Participant
from editorial.models import Project, Story, Item, ItemTemplate, ContentLicense
from task.models import Task
from event.models import Event
from note.models import Note
from discussion.models import Discussion

class BaseOrganization(models.Model):
    """ Abstract of an Organization.
    """

    name = models.CharField(
        max_length=250,
        db_index=True,
    )

    description = models.TextField(
        help_text="Short profile of organization.",
        blank=True,
    )

    owner = models.ForeignKey(
        'Participant',
        help_text='Participant who owns this organization.',
        null=True,
        on_delete = models.SET_NULL,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    website = models.URLField(
        max_length=250,
        blank=True,
    )

    # projects = GenericRelation(Project)

    # items = GenericRelation(Item)

    # item_templates = GenericRelation(ItemTemplate)

    # discussions = GenericRelation(Discussion)

    # notes = GenericRelation(Note)

    # contentlicenses = GenericRelation(ContentLicense)

    # --------------------------------
    # Simple Assets

    # simple assets
    # simple_image_assets = models.ManyToManyField(
    #     'SimpleImage',
    #     related_name='news_organization_simple_image',
    #     blank=True,
    # )

    # simple_document_assets = models.ManyToManyField(
    #     'SimpleDocument',
    #     related_name='news_organization_simple_document',
    #     blank=True,
    # )

    # simple_audio_assets = models.ManyToManyField(
    #     'SimpleAudio',
    #     related_name='news_organization_simple_audio',
    #     blank=True,
    # )

    # simple_video_assets = models.ManyToManyField(
    #     'SimpleVideo',
    #     related_name='news_organization_simple_video',
    #     blank=True,
    # )

    # --------------------------------
    # Logos and Cover Images

    # FIXME Pilkit install
    # logo = models.ImageField(
    #     upload_to='news_organizations',
    #     blank=True,
    # )

    # display_logo = ImageSpecField(
    #     source='logo',
    #     processors=[SmartResize(500, 500)],
    #     format='JPEG',
    # )

    # cover_photo = models.ImageField(
    #     upload_to='org_cover',
    #     blank=True,
    # )

    # display_cover_photo = ImageSpecField(
    #     source='cover_photo',
    #     format='JPEG',
    # )

    class Meta:
        abstract = True
        ordering = ['name']

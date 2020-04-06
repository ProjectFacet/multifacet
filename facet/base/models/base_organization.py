from django.db import models

from base.models import Participant

from .entity_owner import EntityOwner
from .anchor import Anchor
from .partner import Partner
from .network_member import NetworkMember

from editorial.models import Project, Story, Item, ItemTemplate, ContentLicense
from editorial.models import SimpleImage, SimpleDocument, SimpleAudio, SimpleVideo
from task.models import Task
from event.models import Event
from note.models import Note
from discussion.models import Discussion

class BaseOrganization(models.Model):
    """ Abstract of an Organization.
    """

    participant_owner = models.ForeignKey(
        'Participant',
        help_text='Participant who created/owns this organization.',
        null=True,
        on_delete = models.SET_NULL,
    )

    entity_owner_profile = models.OneToOneField(EntityOwner, on_delete=models.CASCADE)
    anchor_profile = models.OneToOneField(Anchor, on_delete=models.CASCADE)
    partner_profile = models.OneToOneField(Partner, on_delete=models.CASCADE)
    network_member_profile = models.OneToOneField(NetworkMember, on_delete=models.CASCADE)

    name = models.CharField(
        max_length=250,
        db_index=True,
    )

    description = models.TextField(
        help_text="Short profile of organization.",
        blank=True,
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

    # notes
    notes = models.ManyToManyField('Note', blank=True)
    # simple assets
    simple_image_assets = models.ManyToManyField(SimpleImage, blank=True)
    simple_document_assets = models.ManyToManyField(SimpleDocument, blank=True)
    simple_audio_assets = models.ManyToManyField(SimpleAudio, blank=True)
    simple_video_assets = models.ManyToManyField(SimpleVideo, blank=True)

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

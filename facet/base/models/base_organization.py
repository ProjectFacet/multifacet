from django.db import models
from django.dispatch import receiver

from .participant import Participant
from .entity_owner import EntityOwner
from .anchor import Anchor
from .partner import Partner
from .network_member import NetworkMember
from note.models import Note


class BaseOrganization(models.Model):
    """ Abstract of an Organization.
    """

    participant_owner = models.ForeignKey(
        Participant,
        help_text='Participant who created/owns this organization.',
        null=True,
        on_delete = models.SET_NULL,
    )

    entity_owner_profile = models.OneToOneField(EntityOwner, null=True, on_delete=models.SET_NULL)
    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)
    partner_profile = models.OneToOneField(Partner, null=True, on_delete=models.SET_NULL)
    network_member_profile = models.OneToOneField(NetworkMember, null=True, on_delete=models.SET_NULL)

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
    notes = models.ManyToManyField(Note, blank=True)
    # internal assets
    internal_image_assets = models.ManyToManyField('editorial.InternalImage', blank=True)
    internal_document_assets = models.ManyToManyField('editorial.InternalDocument', blank=True)
    internal_audio_assets = models.ManyToManyField('editorial.InternalAudio', blank=True)
    internal_video_assets = models.ManyToManyField('editorial.InternalVideo', blank=True)

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

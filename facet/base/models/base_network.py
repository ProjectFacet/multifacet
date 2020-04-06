from django.db import models

from .participant import Participant
from .entity_owner import EntityOwner
from .anchor import Anchor
from .partner import Partner
from editorial.models import SimpleImage, SimpleDocument, SimpleAudio, SimpleVideo

class BaseNetwork(models.Model):
    """A group of organizations, partipants +

    A network is a collection of two or more organizations or participant types.
    """

    #Ownership
    # Participant that owns this network (optional)
    participant_owner = models.ForeignKey(
        Participant,
        help_text='Participant who owns this organization.',
        null=True,
        on_delete = models.SET_NULL,
    )

    # Entity that owns this network (optional)
    entity_owner = ForeignKey(
        EntityOwner,
        help_text='Entity that owns this network.',
        null=True,
        on_delete = models.SET_NULL,
    )

    entity_owner_profile = models.OneToOneField(EntityOwner, on_delete=models.CASCADE)
    anchor_profile = models.OneToOneField(Anchor, on_delete=models.CASCADE)
    partner_profile = models.OneToOneField(Partner, on_delete=models.CASCADE)

    name = models.CharField(
        max_length=350,
        db_index=True,
        help_text="The identifying name of the network."
    )

    description = models.TextField(
        help_text="Short description of the network.",
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    # FIXME Pilkit install
    # logo = models.ImageField(
    #     upload_to='networks',
    #     blank=True,
    # )

    # display_logo = ImageSpecField(
    #     source='logo',
    #     processors=[SmartResize(500, 500)],
    #     format='JPEG',
    # )


    notes = models.ManyToManyField('Note', blank=True)
    # simple assets
    simple_image_assets = models.ManyToManyField(SimpleImage, blank=True)
    simple_document_assets = models.ManyToManyField(SimpleDocument, blank=True)
    simple_audio_assets = models.ManyToManyField(SimpleAudio, blank=True)
    simple_video_assets = models.ManyToManyField(SimpleVideo, blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

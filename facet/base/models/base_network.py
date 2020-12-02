from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from .participant import Participant
from .entity_owner import EntityOwner
from .anchor import Anchor
from .partner import Partner
from .network_member import NetworkMember
from note.models import Note

class BaseNetwork(models.Model):
    """A group of organizations, partipants +

    A network is a collection of two or more organizations or participant types.
    """

    #Ownership
    # Participant that owns this network (optional)
    participant_owner = models.ForeignKey(
        Participant,
        help_text='Participant who owns this network.',
        blank=True,
        null=True,
        on_delete = models.SET_NULL,
    )

    # Entity that owns this network (optional)
    entity_owner = models.ForeignKey(
        EntityOwner,
        related_name='network_owner',
        help_text='Entity that owns this network.',
        null=True,
        on_delete = models.SET_NULL,
    )

    entity_owner_profile = models.OneToOneField(EntityOwner, null=True, on_delete=models.SET_NULL)
    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)
    partner_profile = models.OneToOneField(Partner, null=True, on_delete=models.SET_NULL)

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

    logo = models.ImageField(
        upload_to='networks',
        blank=True,
    )

    display_logo = ImageSpecField(
        source='logo',
        processors=[SmartResize(500, 500)],
        format='JPEG',
    )

    notes = models.ManyToManyField(Note, blank=True)
    # internal assets
    internal_images = models.ManyToManyField('internalasset.InternalImage', blank=True)
    internal_documents = models.ManyToManyField('internalasset.InternalDocument', blank=True)
    internal_audio = models.ManyToManyField('internalasset.InternalAudio', blank=True)
    internal_videos = models.ManyToManyField('internalasset.InternalVideo', blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

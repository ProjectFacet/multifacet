from django.db import models

from base.models import Partner, EntityOwner, Participant
from editorial.models import AudioAsset


class AudioPickupDetailManager(models.Manager):
    """Custom manager for AudioAsset Pickup Details."""

    def create_audioasset_pickup_record(self, original_entity_owner, original_audioasset, partner, partner_audioasset):
        """Method for quick creation of audio pickup detail recod."""
        audioasset_pickup_detail=self.create(original_entity_owner=original_entity_owner, original_audioasset=original_audioasset, partner=partner, partner_audioasset=partner_audioasset)
        return audioasset_pickup_detail


class AudioPickupDetail(models.Model):
    """ The details of each pickup of an AudioAsset."""

    original_participant_owner = models.OneToOneField(
        Participant,
        help_text='Participant that originally created/owned this.',
        null=True,
        on_delete=models.SET_NULL,
    )

    original_participant_owner_name = models.CharField(
        max_length=300,
        help_text='Name of original participant owner.',
        blank=True,
    )

    original_entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that originally made the audio available.',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_entity_owner_name = models.CharField(
        max_length=300,
        help_text='Name of original entity.'
    )

    original_audioasset = models.ForeignKey(
        AudioAsset,
        help_text='Original instance of the audioasset',
        related_name='original_audioasset_detail',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_audioasset_name = models.CharField(
        max_length=300,
        help_text='Title of original audio.'
    )

    partner = models.OneToOneField(
        Partner,
        help_text='Partner picking up the story.',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    partner_name = models.CharField(
        max_length=300,
        help_text='Name of partner.'
    )

    partner_audioasset = models.ForeignKey(
        AudioAsset,
        help_text='The copied version of the audioasset saved by the partner organization.',
        related_name='audioasset_pickup',
        null=True,
        on_delete=models.SET_NULL,
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.',
    )

    objects = AudioPickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickuporg} \'s pickup of audioasset: {audioasset}".format(
                                pickuporg=self.partner.name,
                                audioasset=self.original_audioasset,
        )

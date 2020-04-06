from django.db import models

from base.models import Participant, Partner, EntityOwner
from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset


class AudioPickupDetailManager(models.Manager):
    """Custom manager for AudioAsset Pickup Details."""

    def create_audioasset_pickup_record(self, original_org, original_audioasset, partner, partner_audioasset):
        """Method for quick creation of audio pickup detail recod."""
        audioasset_pickup_detail=self.create(original_org=original_org, original_audioasset=original_audioasset, partner=partner, partner_audioasset=partner_audioasset)
        return audioasset_pickup_detail


@python_2_unicode_compatible
class AudioPickupDetail(models.Model):
    """ The details of each pickup of an AudioAsset."""

    original_org = models.ForeignKey(
        Organization,
        help_text='Organization that originally created the content',
        related_name='original_audioasset_organization',
    )

    original_audioasset = models.ForeignKey(
        AudioAsset,
        help_text='Original instance of the audioasset',
        related_name='original_audioasset_detail',
    )

    partner = models.ForeignKey(
        Organization,
        help_text='Organization that made the pickup.',
        related_name='audioasset_pickup_organization',
    )

    partner_audioasset = models.ForeignKey(
        AudioAsset,
        help_text='The copied version of the audioasset saved by the partner organization.',
        related_name='audioasset_pickup',
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.',
    )

    objects = AudioAssetPickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickuporg} \'s pickup of audioasset: {audioasset}".format(
                                pickuporg=self.partner.name,
                                audioasset=self.original_audioasset,
        )

from django.db import models

from base.models import Participant, Partner, EntityOwner
from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset


class VideoPickupDetailManager(models.Manager):
    """Custom manager for VideoAsset Pickup Details."""

    def create_videoasset_pickup_record(self, original_entity_owner, original_videoasset, partner, partner_videoasset):
        """Method for quick creation of video pickup detail recod."""
        videoasset_pickup_detail=self.create(original_entity_owner=original_entity_owner, original_videoasset=original_videoasset, partner=partner, partner_videoasset=partner_videoasset)
        return videoasset_pickup_detail


class VideoPickupDetail(models.Model):
    """ The details of each pickup of an VideoAsset."""

    original_entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that originally made the item available.',
    )

    original_videoasset = models.ForeignKey(
        VideoAsset,
        help_text='Original instance of the videoasset',
        related_name='original_videoasset_detail',
    )

    partner = models.ManyToManyField(
        Partner,
        related_name='item_pickup_partner',
        help_text='Partner picking up the item.',
        blank=True,
    )

    partner_videoasset = models.ForeignKey(
        VideoAsset,
        help_text='The copied instance of the videoasset saved by the partner organization.',
        related_name='videoasset_pickup',
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.',
    )

    objects = VideoAssetPickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickup_partner} \'s pickup of videoasset: {videoasset}".format(
                                pickup_partner=self.partner.partner_name,
                                videoasset=self.original_videoasset,
        )

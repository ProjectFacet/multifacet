from django.db import models

from base.models import Participant, Partner, EntityOwner
from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset


class ItemPickupDetailManager(models.Manager):
    """Custom manager for Item Pickup Details."""

    def create_item_pickup_record(self, original_entity_owner, partner, original_item, partner_item):
        """Method for quick creation of item pickup detail record."""
        item_pickup_detail=self.create(original_entity_owner=original_entity_owner, partner=partner, original_item=original_item, partner_item=partner_item)
        return item_pickup_detail


class ItemPickupDetail(models.Model):
    """ The details of a each pickup of a item. """

    original_entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that originally made the item available.',
    )

    original_item = models.ForeignKey(
        Item,
        help_text='ID of original instance of the item.',
        related_name='original_item_detail',
    )

    partner = models.ManyToManyField(
        Partner,
        related_name='item_pickup_partner',
        help_text='Partner picking up the item.',
        blank=True,
    )

    partner_item = models.ForeignKey(
        Item,
        help_text='The new version of the item saved by the partner organization.',
        related_name='item_pickup',
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.'
    )

    objects = ItemPickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickup_partner} \'s instance of item: {item}".format(
                                pickup_partner=self.partner.partner_name,
                                item=self.original_item,
                                )

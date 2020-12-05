from django.db import models

from base.models import Partner, EntityOwner, Participant
from editorial.models import Item


class ItemPickupDetailManager(models.Manager):
    """Custom manager for Item Pickup Details."""

    def create_item_pickup_record(self, original_entity_owner, partner, original_item, partner_item):
        """Method for quick creation of item pickup detail record."""
        item_pickup_detail=self.create(original_entity_owner=original_entity_owner, partner=partner, original_item=original_item, partner_item=partner_item)
        return item_pickup_detail


class ItemPickupDetail(models.Model):
    """ The details of each pickup of an item. """

    original_participant_owner = models.OneToOneField(
        Participant,
        help_text='Participant that originally created/owned the item.',
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
        help_text = 'Entity that originally made the item available.',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_entity_owner_name = models.CharField(
        max_length=300,
        help_text='Name of original entity.'
    )

    original_item = models.ForeignKey(
        Item,
        help_text='ID of original instance of the item.',
        related_name='original_item_detail',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_item_name = models.CharField(
        max_length=300,
        help_text='Name of original item.'
    )

    partner = models.OneToOneField(
        Partner,
        related_name='item_pickup_partner',
        help_text='Partner picking up the item.',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    partner_name = models.CharField(
        max_length=300,
        help_text='Name of partner.'
    )

    partner_item = models.ForeignKey(
        Item,
        help_text='The new version of the item saved by the partner organization.',
        related_name='item_pickup',
        null=True,
        on_delete=models.SET_NULL,
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

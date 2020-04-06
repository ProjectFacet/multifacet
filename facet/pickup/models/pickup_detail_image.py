from django.db import models

from base.models import Partner, EntityOwner
from editorial.models import ImageAsset


class ImagePickupDetailManager(models.Manager):
    """Custom manager for ImageAsset Pickup Details."""

    def create_imageasset_pickup_record(self, original_entity_owner, original_imageasset, partner, partner_imageasset):
        """Method for quick creation of image pickup detail recod."""
        imageasset_pickup_detail=self.create(original_entity_owner=original_entity_owner, original_imageasset=original_imageasset, partner=partner, partner_imageasset=partner_imageasset)
        return imageasset_pickup_detail


class ImagePickupDetail(models.Model):
    """ The details of each pickup of an ImageAsset."""

    original_entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that originally made the image available.',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_entity_owner_name = models.CharField(
        max_length=300,
        help_text='Name of original entity.'
    )

    original_imageasset = models.ForeignKey(
        ImageAsset,
        help_text='Original instance of the imageasset',
        related_name='original_imageasset_detail',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_imageasset_name = models.CharField(
        max_length=300,
        help_text='Title of original image.'
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

    partner_imageasset = models.ForeignKey(
        ImageAsset,
        help_text='The copied version of the imageasset saved by the partner organization.',
        related_name='imageasset_pickup',
        null=True,
        on_delete=models.SET_NULL,
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.',
    )

    objects = ImagePickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickuporg} \'s pickup of imageasset: {imageasset}".format(
                                pickuporg=self.partner.name,
                                imageasset=self.original_imageasset,
        )

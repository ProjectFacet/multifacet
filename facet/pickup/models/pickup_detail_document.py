from django.db import models

from base.models import Participant, Partner, EntityOwner
from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset


class DocumentPickupDetailManager(models.Manager):
    """Custom manager for DocumentAsset Pickup Details."""

    def create_documentasset_pickup_record(self, original_org, original_documentasset, partner, partner_documentasset):
        """Method for quick creation of document pickup detail recod."""
        documentasset_pickup_detail=self.create(original_org=original_org, original_documentasset=original_documentasset, partner=partner, partner_documentasset=partner_documentasset)
        return documentasset_pickup_detail


@python_2_unicode_compatible
class DocumentPickupDetail(models.Model):
    """ The details of each pickup of an DocumentAsset."""

    original_org = models.ForeignKey(
        Organization,
        help_text='Organization that originally created the content',
        related_name='original_documentasset_organization',
    )

    original_documentasset = models.ForeignKey(
        DocumentAsset,
        help_text='Original instance of the documentasset',
        related_name='original_documentasset_detail',
    )

    partner = models.ForeignKey(
        Organization,
        help_text='Organization that made the pickup.',
        related_name='pickup_organization',
    )

    partner_documentasset = models.ForeignKey(
        DocumentAsset,
        help_text='The copied instance of the documentasset saved by the partner organization.',
        related_name='documentasset_pickup',
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.',
    )

    objects = DocumentAssetPickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickuporg} \'s pickup of documentasset: {documentasset}".format(
                                pickuporg=self.partner.name,
                                documentasset=self.original_documentasset,
        )

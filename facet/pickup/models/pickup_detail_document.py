from django.db import models

from base.models import Partner, EntityOwner, Participant
from editorial.models import DocumentAsset


class DocumentPickupDetailManager(models.Manager):
    """Custom manager for DocumentAsset Pickup Details."""

    def create_documentasset_pickup_record(self, original_entity_owner, original_documentasset, partner, partner_documentasset):
        """Method for quick creation of document pickup detail recod."""
        documentasset_pickup_detail=self.create(original_entity_owner=original_entity_owner, original_documentasset=original_documentasset, partner=partner, partner_documentasset=partner_documentasset)
        return documentasset_pickup_detail


class DocumentPickupDetail(models.Model):
    """ The details of each pickup of an DocumentAsset."""

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
        help_text = 'Entity that originally made the document available.',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_entity_owner_name = models.CharField(
        max_length=300,
        help_text='Name of original entity.'
    )

    original_documentasset = models.ForeignKey(
        DocumentAsset,
        help_text='Original instance of the documentasset',
        related_name='original_documentasset_detail',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_documentasset_name = models.CharField(
        max_length=300,
        help_text='Title of original document.'
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

    partner_documentasset = models.ForeignKey(
        DocumentAsset,
        help_text='The copied version of the documentasset saved by the partner organization.',
        related_name='documentasset_pickup',
        null=True,
        on_delete=models.SET_NULL,
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.',
    )

    objects = DocumentPickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickuporg} \'s pickup of documentasset: {documentasset}".format(
                                pickuporg=self.partner.name,
                                documentasset=self.original_documentasset,
        )

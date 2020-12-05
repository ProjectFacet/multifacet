from django.db import models

from base.models import Partner, EntityOwner, Participant
from editorial.models import VideoAsset


class VideoPickupDetailManager(models.Manager):
    """Custom manager for VideoAsset Pickup Details."""

    def create_videoasset_pickup_record(self, original_entity_owner, original_videoasset, partner, partner_videoasset):
        """Method for quick creation of video pickup detail recod."""
        videoasset_pickup_detail=self.create(original_entity_owner=original_entity_owner, original_videoasset=original_videoasset, partner=partner, partner_videoasset=partner_videoasset)
        return videoasset_pickup_detail


class VideoPickupDetail(models.Model):
    """The details of each pickup of an VideoAsset."""

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
        help_text = 'Entity that originally made the video available.',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_entity_owner_name = models.CharField(
        max_length=300,
        help_text='Name of original entity.'
    )

    original_videoasset = models.ForeignKey(
        VideoAsset,
        help_text='Original instance of the videoasset',
        related_name='original_videoasset_detail',
        null=True,
        on_delete=models.SET_NULL,
    )

    # To capture name of entity in the event the entity records are deleted.
    # FIXME Better ways to manage this data integrity component?
    original_videoasset_name = models.CharField(
        max_length=300,
        help_text='Title of original video.'
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

    partner_videoasset = models.ForeignKey(
        VideoAsset,
        help_text='The copied version of the videoasset saved by the partner organization.',
        related_name='videoasset_pickup',
        null=True,
        on_delete=models.SET_NULL,
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.',
    )

    objects = VideoPickupDetailManager()

    def __str__(self):
        return "Pickup info for {pickup_partner} \'s pickup of videoasset: {videoasset}".format(
                                pickup_partner=self.partner.partner_name,
                                videoasset=self.original_videoasset,
        )

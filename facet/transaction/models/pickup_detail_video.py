# from django.db import models
#
# from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset
# from entity.models import NewsOrganization
# from base.models import Participant
#
# class VideoPickupDetailManager(models.Manager):
#     """Custom manager for VideoAsset Pickup Details."""
#
#     def create_videoasset_pickup_record(self, original_org, original_videoasset, partner, partner_videoasset):
#         """Method for quick creation of video pickup detail recod."""
#         videoasset_pickup_detail=self.create(
#                                         original_org=original_org,
#                                         original_videoasset=original_videoasset,
#                                         partner=partner,
#                                         partner_videoasset=partner_videoasset)
#         return videoasset_pickup_detail
#
#
# @python_2_unicode_compatible
# class VideoPickupDetail(models.Model):
#     """ The details of each pickup of an VideoAsset."""
#
#     original_org = models.ForeignKey(
#         Organization,
#         help_text='Organization that originally created the content',
#         related_name='original_videoasset_organization',
#     )
#
#     original_videoasset = models.ForeignKey(
#         VideoAsset,
#         help_text='Original instance of the videoasset',
#         related_name='original_videoasset_detail',
#     )
#
#     partner = models.ForeignKey(
#         Organization,
#         help_text='Organization that made the pickup.',
#         related_name='videoasset_pickup_organization',
#     )
#
#     partner_videoasset = models.ForeignKey(
#         VideoAsset,
#         help_text='The copied instance of the videoasset saved by the partner organization.',
#         related_name='videoasset_pickup',
#     )
#
#     pickup_date = models.DateTimeField(
#         auto_now_add=True,
#         help_text='Datetime when pickup was made.',
#     )
#
#     objects = VideoAssetPickupDetailManager()
#
#     def __str__(self):
#         return "Pickup info for {pickuporg} \'s pickup of videoasset: {videoasset}".format(
#                                 pickuporg=self.partner.name,
#                                 videoasset=self.original_videoasset,
#         )

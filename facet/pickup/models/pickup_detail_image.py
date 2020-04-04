# from django.db import models
#
# from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset
# from entity.models import NewsOrganization
# from base.models import Participant
#
# class ImagePickupDetailManager(models.Manager):
#     """Custom manager for ImageAsset Pickup Details."""
#
#     def create_imageasset_pickup_record(self, original_org, original_imageasset, partner, partner_imageasset):
#         """Method for quick creation of image pickup detail recod."""
#         imageasset_pickup_detail=self.create(
#                                         original_org=original_org,
#                                         original_imageasset=original_imageasset,
#                                         partner=partner,
#                                         partner_imageasset=partner_imageasset)
#         return imageasset_pickup_detail
#
#
# @python_2_unicode_compatible
# class ImagePickupDetail(models.Model):
#     """ The details of each pickup of an ImageAsset."""
#
#     original_org = models.ForeignKey(
#         Organization,
#         help_text='Organization that originally created the content',
#         related_name='original_imageasset_organization',
#     )
#
#     original_imageasset = models.ForeignKey(
#         ImageAsset,
#         help_text='Original instance of the imageasset',
#         related_name='original_imageasset_detail',
#     )
#
#     partner = models.ForeignKey(
#         Organization,
#         help_text='Organization that made the pickup.',
#         related_name='pickup_organization',
#     )
#
#     partner_imageasset = models.ForeignKey(
#         ImageAsset,
#         help_text='The copied instance of the imageasset saved by the partner organization.',
#         related_name='imageasset_pickup',
#     )
#
#     pickup_date = models.DateTimeField(
#         auto_now_add=True,
#         help_text='Datetime when pickup was made.',
#     )
#
#     objects = ImageAssetPickupDetailManager()
#
#     def __str__(self):
#         return "Pickup info for {pickuporg} \'s pickup of imageasset: {imageasset}".format(
#                                 pickuporg=self.partner.name,
#                                 imageasset=self.original_imageasset,
#         )

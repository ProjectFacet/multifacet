# from django.db import models
#
# from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset
# from entity.models import NewsOrganization
# from base.models import Participant
#
# class ItemPickupDetailManager(models.Manager):
#     """Custom manager for Item Pickup Details."""
#
#     def create_item_pickup_record(self, original_org, partner, original_item, partner_item):
#         """Method for quick creation of item pickup detail record."""
#         item_pickup_detail=self.create(original_org=original_org, partner=partner, original_item=original_item, partner_item=partner_item)
#         return item_pickup_detail
#
#
# @python_2_unicode_compatible
# class ItemPickupDetail(models.Model):
#     """ The details of a each pickup of a item. """
#
#     original_org = models.ForeignKey(
#         Organization,
#         help_text='Organization that originally created the content.',
#         related_name='original_item_organization',
#     )
#
#     original_item = models.ForeignKey(
#         Item,
#         help_text='Original instance of the item.',
#         related_name='original_item_detail',
#     )
#
#     partner = models.ForeignKey(
#         Organization,
#         help_text='Organization that picked up the item.',
#         related_name='pickup_organization',
#     )
#
#     partner_item = models.ForeignKey(
#         Item,
#         help_text='The new version of the item saved by the partner organization.',
#         related_name='item_pickup',
#     )
#
#     pickup_date = models.DateTimeField(
#         auto_now_add=True,
#         help_text='Datetime when pickup was made.'
#     )
#
#     objects = ItemPickupDetailManager()
#
#     def __str__(self):
#         return "Pickup info for {pickuporg} \'s instance of item: {item}".format(
#                                 pickuporg=self.partner.name,
#                                 item=self.original_item,
#                                 )

# from django.db import models
#
# from base.models import Participant
# from entity.models import NewsOrganization
# from .asset_base import BaseAsset, BaseAssetMetadata
# from .tag import Tag
#
# class BaseImage(BaseAsset):
#     """Base class for image assets (an image with some metadata).
#
#     Used for ImageAssets (attached to items) as well as SimpleAssets
#     (attached for tasks, notes, etc).
#     """
#
#     # type name for search system
#     type = "Image"
#
#     image = models.ImageField(
#         upload_to='photos',
#         blank=True,
#     )
#
#     display_images = ImageSpecField(
#         source='images',
#         format='JPEG',
#     )
#
#     class Meta:
#         abstract = True
#
#
# class ImageAssetManager(models.Manager):
#     """Custom manager for ImageAsset."""
#
#     def create_imageasset(self, owner, content_object, title, description, attribution, photo, asset_type):
#         """Method for quick creation of an image asset."""
#
#         imageasset=self.create(owner=owner, content_object=content_object, title=title, description=description, attribution=attribution, photo=photo, asset_type=asset_type)
#         return imageasset
#
#
# class ImageAsset(BaseImage, BaseAssetMetadata):
#     """ Uploaded Image Asset for a item. """
#
#     #Choices for Asset type
#     PHOTO = 'PIC'
#     GRAPHIC = 'GRAPH'
#
#     ASSET_TYPE_CHOICES = (
#         (PHOTO, 'Photograph'),
#         (GRAPHIC, 'Graphic or Illustration'),
#     )
#
#     asset_type = models.CharField(
#         max_length=20,
#         choices = ASSET_TYPE_CHOICES,
#         help_text='The kind of image.'
#     )
#
#     objects = ImageAssetManager()
#
#     def get_image_usage(self):
#         """Return items an image is associated with."""
#         return self.item_set.all()
#
#     # def get_absolute_url(self):
#     #     return reverse('image_asset_detail', kwargs={'pk': self.id})
#
#     @property
#     def type(self):
#         return "ImageAsset"
#
#
# class SimpleImage(BaseImage):
#     """Simple image (with some metadata) for attaching to tasks, events, etc."""
#
#     def get_usage(self):
#         """Return Organizations, Networks, Projects, Events and Tasks
#         the simple asset is associated with."""
#
#         associations = []
#         orgs = self.organization_simple_image.all()
#         networks = self.network_set.all()
#         projects = self.project_set.all()
#         events = self.event_set.all()
#         tasks = self.event_set.all()
#         associations.extend(orgs)
#         associations.extend(networks)
#         associations.extend(projects)
#         associations.extend(events)
#         associations.extend(tasks)
#
#         return associations
#
#     # def get_absolute_url(self):
#     #     return reverse('simple_image_detail', kwargs={'pk': self.id})
#
#     @property
#     def type(self):
#         return "SimpleImage"

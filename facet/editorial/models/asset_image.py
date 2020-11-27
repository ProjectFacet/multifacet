from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from base.models import BaseAssetMetadata, BaseImage


class ImageAssetManager(models.Manager):
    """Custom manager for ImageAsset."""

    def create_imageasset(self, participantowner, entity_owner, title, description, attribution, photo, asset_type):
        """Method for quick creation of an image asset."""

        imageasset=self.create(participant_owner=participant_owner, entity_owner=entity_owner, title=title, description=description, attribution=attribution, photo=photo, asset_type=asset_type)
        return imageasset


class ImageAsset(BaseImage, BaseAssetMetadata):
    """ Uploaded Image Asset for a item. """

    #Choices for Asset type
    PHOTO = 'PHOTO'
    GRAPHIC = 'GRAPHIC'

    ASSET_TYPE_CHOICES = (
        (PHOTO, 'Photograph'),
        (GRAPHIC, 'Graphic or Illustration'),
    )

    asset_type = models.CharField(
        max_length=20,
        choices = ASSET_TYPE_CHOICES,
        help_text='The kind of image.'
    )

    # TODO to be populated automatically
    file_type = models.CharField(
        max_length=10,
        help_text='The file extension'
    )

    # TODO to be populated automatically
    file_size = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='Size of uploaded file.'
    )

    objects = ImageAssetManager()

    def get_image_usage(self):
        """Return items an image is associated with."""
        return self.item_set.all()

    # def get_absolute_url(self):
    #     return reverse('image_asset_detail', kwargs={'pk': self.id})

    @property
    def type(self):
        return "Image Asset"

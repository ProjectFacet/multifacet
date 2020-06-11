from django.db import models

from .asset_base import BaseAsset, BaseAssetMetadata


class BaseImage(BaseAsset):
    """Base class for image assets (an image with some metadata).

    Used for ImageAssets (attached to items) as well as SimpleAssets
    (attached for tasks, notes, etc).
    """

    # type name for search system
    type = "Image"

    # image = models.ImageField(
    #     upload_to='photos',
    #     blank=True,
    # )
    #
    # display_images = ImageSpecField(
    #     source='images',
    #     format='JPEG',
    # )

    class Meta:
        abstract = True


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


class InternalImage(BaseImage):
    """Simple image (with some metadata) for attaching to tasks, events, etc."""

    def get_usage(self):
        """Return Organizations, Networks, Projects, Events and Tasks
        the internal asset is associated with."""

        associations = []
        orgs = self.organization_internal_image.all()
        networks = self.network_set.all()
        projects = self.project_set.all()
        events = self.event_set.all()
        tasks = self.event_set.all()
        associations.extend(orgs)
        associations.extend(networks)
        associations.extend(projects)
        associations.extend(events)
        associations.extend(tasks)

        return associations

    # def get_absolute_url(self):
    #     return reverse('internal_image_detail', kwargs={'pk': self.id})

    @property
    def type(self):
        return "Simple Image"

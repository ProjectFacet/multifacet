from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from base.models import BaseAssetMetadata, BaseVideo


class VideoAssetManager(models.Manager):
    """Custom manager for VideoAsset."""

    def create_videoasset(self, participant_owner, entity_owner, title, description, attribution, video, asset_type):
        """Method for quick creation of a video asset."""
        videoasset=self.create(participant_owner=participant_owner, entity_owner=entity_owner, title=title, description=description, attribution=attribution, video=video, asset_type=asset_type)
        return videoasset


class VideoAsset(BaseVideo, BaseAssetMetadata):
    """ Uploaded Video Asset. """

    #Choices for Asset type
    MP4 = 'MP4'
    YT = 'YOUTUBE'
    VIM = 'VIMEO'

    ASSET_TYPE_CHOICES = (
        (MP4, 'mp4'),
        (YT, 'YouTube'),
        (VIM, 'Vimeo')
    )

    asset_type = models.CharField(
        max_length=20,
        choices = ASSET_TYPE_CHOICES,
        help_text='The kind of video.'
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

    objects = VideoAssetManager()

    def get_video_usage(self):
        """Return items an video file is associated with."""
        return self.item_set.all()

    # def get_absolute_url(self):
    #     return reverse('video_asset_detail', kwargs={'pk': self.id})

    @property
    def type(self):
        return "Video Asset"

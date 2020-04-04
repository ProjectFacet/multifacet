# from django.db import models
#
# from base.models import Participant
# from entity.models import NewsOrganization
# from .asset_base import BaseAsset, BaseAssetMetadata
# from .tag import Tag
#
#
# class BaseVideo(BaseAsset):
#     """Base class for videos.
#
#     Subclassed by VideoAsset and SimpleVideo.
#     """
#
#     # metadata for search system
#     type = "Video"
#
#     video = models.FileField(
#         upload_to='videos',
#         blank=True,
#     )
#
#     # poster = models.FileField(
#     #     upload_to='videos',
#     #     blank=True,
#     # )
#
#     link = models.URLField(
#         max_length=400,
#         help_text='Link to video file on YouTube or Vimeo',
#         blank=True,
#     )
#
#     class Meta:
#         abstract = True
#
#
# class VideoAssetManager(models.Manager):
#     """Custom manager for VideoAsset."""
#
#     def create_videoasset(self, owner, content_object, title, description, attribution, video, asset_type):
#         """Method for quick creation of a video asset."""
#         videoasset=self.create(owner=owner, content_object=content_object, title=title, description=description, attribution=attribution, video=video, asset_type=asset_type)
#         return videoasset
#
#
# class VideoAsset(BaseVideo, BaseAssetMetadata):
#     """ Uploaded Video Asset. """
#
#     #Choices for Asset type
#     MP4 = 'MP4'
#     YT = 'YOUTUBE'
#     VIM = 'VIMEO'
#
#     ASSET_TYPE_CHOICES = (
#         (MP4, 'mp4'),
#         (YT, 'YouTube'),
#         (VIM, 'Vimeo')
#     )
#
#     asset_type = models.CharField(
#         max_length=20,
#         choices = ASSET_TYPE_CHOICES,
#         help_text='The kind of video.'
#     )
#
#     objects = VideoAssetManager()
#
#     def get_video_usage(self):
#         """Return items an video file is associated with."""
#         return self.item_set.all()
#
#     # def get_absolute_url(self):
#     #     return reverse('video_asset_detail', kwargs={'pk': self.id})
#
#     @property
#     def type(self):
#         return "VideoAsset"
#
#
# class SimpleVideo(BaseVideo):
#     """Uploaded video (attaches to tasks, events, etc)"""
#
#     def get_usage(self):
#         """Return Organizations, Networks, Projects, Events and Tasks
#         the simple asset is associated with."""
#
#         associations = []
#         orgs = self.organization_simple_video.all()
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
#
#     @property
#     def type(self):
#         return "SimpleVideo"

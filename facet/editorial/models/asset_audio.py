# from django.db import models
#
# from base.models import Participant
# from entity.models import NewsOrganization
# from .asset_base import BaseAsset, BaseAssetMetadata
# from .tag import Tag
#
#
# class BaseAudio(BaseAsset):
#     """Base type for audio files.
#
#     Subclassed by AudioAsset and SimpleAudio.
#     """
#
#     # metadata for search system
#     type = "Audio"
#
#     audio = models.FileField(
#         upload_to='audio',
#         blank=True,
#     )
#
#     link = models.URLField(
#         max_length=400,
#         help_text='Link to audio file on SoundCloud',
#         blank=True,
#     )
#
#     class Meta:
#         abstract = True
#
#
# class AudioAssetManager(models.Manager):
#     """Custom manager for AudioAsset."""
#
#     def create_audioasset(self, owner, content_object, title, description, attribution, audio, asset_type):
#         """Method for quick creation of a audio asset."""
#         audioasset=self.create(owner=owner, content_object=content_object, title=title, description=description, attribution=attribution, audio=audio, asset_type=asset_type)
#         return audioasset
#
#
# class AudioAsset(BaseAudio, BaseAssetMetadata):
#     """Audio asset (attaches to a item)"""
#
#     #Choices for Asset type
#     MP3 = 'MP3'
#     WAV = 'WAV'
#     SOUNDCLOUD = 'SC'
#
#     ASSET_TYPE_CHOICES = (
#         (MP3, 'mp3'),
#         (WAV, 'wav'),
#         (SOUNDCLOUD, 'SoundCloud')
#     )
#
#     asset_type = models.CharField(
#         max_length=20,
#         choices = ASSET_TYPE_CHOICES,
#         help_text='The kind of audio.'
#     )
#
#     objects = AudioAssetManager()
#
#     def get_audio_usage(self):
#         """Return items an audio file is associated with."""
#         return self.item_set.all()
#
#     # def get_absolute_url(self):
#     #     return reverse('audio_asset_detail', kwargs={'pk': self.id})
#
#     @property
#     def type(self):
#         return "AudioAsset"
#
#
# class SimpleAudio(BaseAudio):
#     """Simple Audio (attaches to an event, task, etc.)"""
#
#     def get_usage(self):
#         """Return Organizations, Networks, Projects, Events and Tasks
#         the simple asset is associated with."""
#
#         associations = []
#         orgs = self.organization_simple_audio.all()
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
#     #     return reverse('simple_audio_detail', kwargs={'pk': self.id})
#
#     @property
#     def type(self):
#         return "SimpleAudio"

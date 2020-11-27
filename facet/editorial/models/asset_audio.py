from django.db import models

from base.models import BaseAssetMetadata, BaseAudio


class AudioAssetManager(models.Manager):
    """Custom manager for AudioAsset."""

    def create_audioasset(self, participant_owner, entity_owner, title, description, attribution, audio, asset_type):
        """Method for quick creation of a audio asset."""
        audioasset=self.create(participant_owner=participant_owner, entity_owner=entity_owner, title=title, description=description, attribution=attribution, audio=audio, asset_type=asset_type)
        return audioasset


class AudioAsset(BaseAudio, BaseAssetMetadata):
    """Audio asset (attaches to a item)"""

    #Choices for Asset type
    MP3 = 'MP3'
    WAV = 'WAV'
    SOUNDCLOUD = 'SC'

    ASSET_TYPE_CHOICES = (
        (MP3, 'mp3'),
        (WAV, 'wav'),
        (SOUNDCLOUD, 'SoundCloud')
    )

    asset_type = models.CharField(
        max_length=20,
        choices = ASSET_TYPE_CHOICES,
        help_text='The kind of audio.'
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

    objects = AudioAssetManager()

    def get_audio_usage(self):
        """Return items an audio file is associated with."""
        return self.item_set.all()

    # def get_absolute_url(self):
    #     return reverse('audio_asset_detail', kwargs={'pk': self.id})

    @property
    def type(self):
        return "Audio Asset"

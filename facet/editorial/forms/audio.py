"""Forms for Assets and related entities."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from editorial.models import (
    AudioAsset,
    SimpleAudio,
)

from editorial.widgets import (
    _TextInput,
    _Textarea,
    _Select,
)


class AudioAssetForm(forms.ModelForm):
    """Upload audio to an item."""

    class Meta:
        model = AudioAsset

        fields = [
            'title',
            'description',
            'attribution',
            # 'audio',
            'link',
            'asset_type',
            # 'senstive',
        ]

        widgets = {
            'title': _TextInput('Asset Title'),
            'description': _Textarea('Description', rows=3),
            'attribution': _Textarea('Attribution', rows=3),
            'link': _TextInput('Link'),
            'asset_type': _Select(),
            # 'sensitive': CheckboxInput(),
        }


##############################################################################################
# Associating Forms: associating existing library assets to an item.

class LibraryAudioAssociateForm(Form):
    """Form for adding existing library audios to an item."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to primary owner's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(LibraryAudioAssociateForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['audios'] = forms.ModelMultipleChoiceField(
                queryset=org.audioasset_set.all(),
                required=False)
        elif participant:
            self.fields['audios'] = forms.ModelMultipleChoiceField(
                queryset=participant.audioasset_set.all(),
                required=False)


class SimpleAudioForm(forms.ModelForm):
    """Upload a simple audio."""

    class Meta:
        model = SimpleAudio

        fields = [
            'title',
            'description',
            'audio',
        ]

        widgets = {
            'title': _TextInput('Title'),
            'description': _Textarea('Description', rows=3),
        }


class SimpleAudioLibraryAssociateForm(Form):
    """Form for adding existing simple audios to an Organization, Network,
    Project, Series, Task or Event."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to organization's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(SimpleAudioLibraryAssociateForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['simpleaudios'] = forms.ModelMultipleChoiceField(
                queryset=org.simpleaudio_set.all(),
                required=False)
        elif participant:
            self.fields['simpleaudios'] = forms.ModelMultipleChoiceField(
                queryset=participant.simpleaudio_set.all(),
                required=False)

"""Forms for Assets and related entities."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from editorial.models import (
    VideoAsset,
    SimpleVideo,
)

from editorial.widgets import (
    _TextInput,
    _Textarea,
    _Select,
)


class VideoAssetForm(forms.ModelForm):
    """Upload video to an item."""

    class Meta:
        model = VideoAsset

        fields = [
            'title',
            'description',
            'attribution',
            # 'video',
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

class LibraryVideoAssociateForm(Form):
    """Form for adding existing library videos to an item."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to primary owner's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(LibraryVideoAssociateForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['videos'] = forms.ModelMultipleChoiceField(
                queryset=org.videoasset_set.all(),
                required=False)
        elif participant:
            self.fields['videos'] = forms.ModelMultipleChoiceField(
                queryset=participant.videoasset_set.all(),
                required=False)


class SimpleVideoForm(forms.ModelForm):
    """Upload a simple video."""

    class Meta:
        model = SimpleVideo

        fields = [
            'title',
            'description',
            'video',
        ]

        widgets = {
            'title': _TextInput('Title'),
            'description': _Textarea('Description', rows=3),
        }


class SimpleVideoLibraryAssociateForm(Form):
    """Form for adding existing simple videos to an Organization, Network,
    Project, Series, Task or Event."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to organization's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(SimpleVideoLibraryAssociateForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['simplevideos'] = forms.ModelMultipleChoiceField(
                queryset=org.simplevideo_set.all(),
                required=False)
        elif participant:
            self.fields['simplevideos'] = forms.ModelMultipleChoiceField(
                queryset=participant.simplevideo_set.all(),
                required=False)

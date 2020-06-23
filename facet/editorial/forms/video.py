"""Forms for Assets and related entities."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from editorial.models import (
    VideoAsset,
    InternalVideo,
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

        if entity.newsorganization:
            self.fields['video'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganization.videoasset_set.all(),
                required=False)
        elif entity.newsorganizationnetwork:
            self.fields['video'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganizationnetwork.videoasset_set.all(),
                required=False)
        elif participant.staffjournalist:
            self.fields['video'] = forms.ModelMultipleChoiceField(
                queryset=participant.staffjournalist.newsorganization.videoasset_set.all(),
                required=False)
        elif participant.unaffiliatedstaffjournalist:
            self.fields['video'] = forms.ModelMultipleChoiceField(
                queryset=participant.videoasset_set.all(),
                required=False)
        elif participant.freelancejournalist:
            self.fields['video'] = forms.ModelMultipleChoiceField(
                queryset=participant.videoasset_set.all(),
                required=False)


class InternalVideoForm(forms.ModelForm):
    """Upload a internal video."""

    class Meta:
        model = InternalVideo

        fields = [
            'title',
            'description',
            'video',
        ]

        widgets = {
            'title': _TextInput('Title'),
            'description': _Textarea('Description', rows=3),
        }


class InternalVideoLibraryAssociateForm(Form):
    """Form for adding existing internal videos to an Organization, Network,
    Project, Series, Task or Event."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to organization's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(InternalVideoLibraryAssociateForm, self).__init__(*args, **kwargs)

        if entity.newsorganization:
            self.fields['internalvideo'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganization.internalvideo_set.all(),
                required=False)
        elif entity.newsorganizationnetwork:
            self.fields['internalvideo'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganizationnetwork.internalvideo_set.all(),
                required=False)
        elif participant.staffjournalist:
            self.fields['internalvideo'] = forms.ModelMultipleChoiceField(
                queryset=participant.staffjournalist.newsorganization.internalvideo_set.all(),
                required=False)
        elif participant.unaffiliatedstaffjournalist:
            self.fields['internalvideo'] = forms.ModelMultipleChoiceField(
                queryset=participant.internalvideo_set.all(),
                required=False)
        elif participant.freelancejournalist:
            self.fields['internalvideo'] = forms.ModelMultipleChoiceField(
                queryset=participant.internalvideo_set.all(),
                required=False)

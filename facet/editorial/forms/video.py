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

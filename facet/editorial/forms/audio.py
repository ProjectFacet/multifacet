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
    AudioAsset,
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


class LibraryAudioAssociateForm(Form):
    """Form for adding existing library audios to an item."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to primary owner's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(LibraryAudioAssociateForm, self).__init__(*args, **kwargs)

        if entity.newsorganization:
            self.fields['audio'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganization.audioasset_set.all(),
                required=False)
        elif entity.newsorganizationnetwork:
            self.fields['audio'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganizationnetwork.audioasset_set.all(),
                required=False)
        elif participant.staffjournalist:
            self.fields['audio'] = forms.ModelMultipleChoiceField(
                queryset=participant.staffjournalist.newsorganization.audioasset_set.all(),
                required=False)
        elif participant.unaffiliatedstaffjournalist:
            self.fields['audio'] = forms.ModelMultipleChoiceField(
                queryset=participant.audioasset_set.all(),
                required=False)
        elif participant.freelancejournalist:
            self.fields['audio'] = forms.ModelMultipleChoiceField(
                queryset=participant.audioasset_set.all(),
                required=False)

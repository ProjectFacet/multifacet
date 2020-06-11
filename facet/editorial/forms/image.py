"""Forms for Assets and related entities."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from editorial.models import (
    ImageAsset,
    InternalImage,
)

from editorial.widgets import (
    _TextInput,
    _Textarea,
    _Select,
)


class ImageAssetForm(forms.ModelForm):
    """Upload image to an item."""

    class Meta:
        model = ImageAsset

        fields = [
            'title',
            'description',
            'attribution',
            # 'photo',
            'asset_type',
            # 'senstive',
        ]

        widgets = {
            'title': _TextInput('Asset Title'),
            'description': _Textarea('Description', rows=3),
            'attribution': _Textarea('Attribution', rows=3),
            'asset_type': _Select(),
            # 'sensitive': CheckboxInput(),
        }


##############################################################################################
# Associating Forms: associating existing library assets to an item.

class LibraryImageAssociateForm(Form):
    """Form for adding existing library images to an item."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to primary owner's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(LibraryImageAssociateForm, self).__init__(*args, **kwargs)

        if entity.newsorganization:
            self.fields['images'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganization.imageasset_set.all(),
                required=False)
        elif entity.newsorganizationnetwork:
            self.fields['images'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganizationnetwork.imageasset_set.all(),
                required=False)
        elif participant.staffjournalist:
            self.fields['images'] = forms.ModelMultipleChoiceField(
                queryset=participant.staffjournalist.newsorganization.imageasset_set.all(),
                required=False)
        elif participant.unaffiliatedstaffjournalist:
            self.fields['images'] = forms.ModelMultipleChoiceField(
                queryset=participant.imageasset_set.all(),
                required=False)
        elif participant.freelancejournalist:
            self.fields['images'] = forms.ModelMultipleChoiceField(
                queryset=participant.imageasset_set.all(),
                required=False)


class InternalImageForm(forms.ModelForm):
    """Upload a internal image."""

    class Meta:
        model = InternalImage

        fields = [
            'title',
            'description',
            # 'photo',
        ]

        widgets = {
            'title': _TextInput('Title'),
            'description': _Textarea('Description', rows=3),
        }


class InternalImageLibraryAssociateForm(Form):
    """Form for adding existing internal images to an Organization, Network,
    Project, Series, Task or Event."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to organization's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(InternalImageLibraryAssociateForm, self).__init__(*args, **kwargs)

        if entity.newsorganization:
            self.fields['internalimages'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganization.internalimage_set.all(),
                required=False)
        elif entity.newsorganizationnetwork:
            self.fields['internalimages'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganizationnetwork.internalimage_set.all(),
                required=False)
        elif participant.staffjournalist:
            self.fields['internalimages'] = forms.ModelMultipleChoiceField(
                queryset=participant.staffjournalist.newsorganization.internalimage_set.all(),
                required=False)
        elif participant.unaffiliatedstaffjournalist:
            self.fields['internalimages'] = forms.ModelMultipleChoiceField(
                queryset=participant.internalimage_set.all(),
                required=False)
        elif participant.freelancejournalist:
            self.fields['internalimages'] = forms.ModelMultipleChoiceField(
                queryset=participant.internalimage_set.all(),
                required=False)

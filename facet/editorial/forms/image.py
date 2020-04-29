"""Forms for Assets and related entities."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from editorial.models import (
    ImageAsset,
    SimpleImage,
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

        if entity:
            self.fields['images'] = forms.ModelMultipleChoiceField(
                queryset=org.imageasset_set.all(),
                required=False)
        elif participant:
            self.fields['images'] = forms.ModelMultipleChoiceField(
                queryset=participant.imageasset_set.all(),
                required=False)


class SimpleImageForm(forms.ModelForm):
    """Upload a simple image."""

    class Meta:
        model = SimpleImage

        fields = [
            'title',
            'description',
            # 'photo',
        ]

        widgets = {
            'title': _TextInput('Title'),
            'description': _Textarea('Description', rows=3),
        }


class SimpleImageLibraryAssociateForm(Form):
    """Form for adding existing simple images to an Organization, Network,
    Project, Series, Task or Event."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to organization's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(SimpleImageLibraryAssociateForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['simpleimages'] = forms.ModelMultipleChoiceField(
                queryset=org.simpleimage_set.all(),
                required=False)
        elif participant:
            self.fields['simpleimages'] = forms.ModelMultipleChoiceField(
                queryset=participant.simpleimage_set.all(),
                required=False)

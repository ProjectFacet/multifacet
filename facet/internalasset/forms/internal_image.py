"""Forms for Assets and related entities."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from internalasset.models import (
    InternalImage,
)


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

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
    InternalVideo,
)


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

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
    InternalDocument,
)


class InternalDocumentForm(forms.ModelForm):
    """Upload a internal document."""

    class Meta:
        model = InternalDocument

        fields = [
            'title',
            'description',
            'document',
        ]

        widgets = {
            'title': _TextInput('Title'),
            'description': _Textarea('Description', rows=3),
        }


class InternalDocumentLibraryAssociateForm(Form):
    """Form for adding existing internal documents to an Organization, Network,
    Project, Series, Task or Event."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to organization's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(InternalDocumentLibraryAssociateForm, self).__init__(*args, **kwargs)

        if entity.newsorganization:
            self.fields['internaldocuments'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganization.internaldocument_set.all(),
                required=False)
        elif entity.newsorganizationnetwork:
            self.fields['internaldocuments'] = forms.ModelMultipleChoiceField(
                queryset=entity.newsorganizationnetwork.internaldocument_set.all(),
                required=False)
        elif participant.staffjournalist:
            self.fields['internaldocuments'] = forms.ModelMultipleChoiceField(
                queryset=participant.staffjournalist.newsorganization.internaldocument_set.all(),
                required=False)
        elif participant.unaffiliatedstaffjournalist:
            self.fields['internaldocuments'] = forms.ModelMultipleChoiceField(
                queryset=participant.internaldocument_set.all(),
                required=False)
        elif participant.freelancejournalist:
            self.fields['internaldocuments'] = forms.ModelMultipleChoiceField(
                queryset=participant.internaldocument_set.all(),
                required=False)

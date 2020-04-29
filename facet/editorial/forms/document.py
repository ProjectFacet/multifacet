"""Forms for Assets and related entities."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from editorial.models import (
    DocumentAsset,
    SimpleDocument,
)

from editorial.widgets import (
    _TextInput,
    _Textarea,
    _Select,
)


class DocumentAssetForm(forms.ModelForm):
    """Upload document to an item."""

    class Meta:
        model = DocumentAsset

        fields = [
            'title',
            'description',
            'attribution',
            # 'document',
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

class LibraryDocumentAssociateForm(Form):
    """Form for adding existing library documents to an item."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to primary owner's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(LibraryDocumentAssociateForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['documents'] = forms.ModelMultipleChoiceField(
                queryset=org.documentasset_set.all(),
                required=False)
        elif participant:
            self.fields['documents'] = forms.ModelMultipleChoiceField(
                queryset=participant.documentasset_set.all(),
                required=False)


class SimpleDocumentForm(forms.ModelForm):
    """Upload a simple document."""

    class Meta:
        model = SimpleDocument

        fields = [
            'title',
            'description',
            'document',
        ]

        widgets = {
            'title': _TextInput('Title'),
            'description': _Textarea('Description', rows=3),
        }


class SimpleDocumentLibraryAssociateForm(Form):
    """Form for adding existing simple documents to an Organization, Network,
    Project, Series, Task or Event."""

    def __init__(self, *args, **kwargs):
        """Add field with vocabulary set to organization's assets."""

        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        super(SimpleDocumentLibraryAssociateForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['simpledocuments'] = forms.ModelMultipleChoiceField(
                queryset=org.simpledocument_set.all(),
                required=False)
        elif participant:
            self.fields['simpledocuments'] = forms.ModelMultipleChoiceField(
                queryset=participant.simpledocument_set.all(),
                required=False)

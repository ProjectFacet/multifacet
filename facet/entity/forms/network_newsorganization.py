"""Forms for News Organizations and related functionality."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from entity.models import (
    NewsOrganizationNetwork,
)


class NewsOrganizationNetworkForm(forms.ModelForm):
    """Form to create or update a NewsOrganizationNetwork."""

    class Meta:
        model = NewsOrganization
        fields = ['name', 'description', 'logo']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

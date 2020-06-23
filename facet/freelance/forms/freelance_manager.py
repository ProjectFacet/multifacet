"""Forms for Freelance Managers and related functionality."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from freelance.models import (
    FreelanceManager,
)


class FreelanceManagerForm(forms.ModelForm):
    """Form to create or update a Freelance Journalist."""

    class Meta:
        model = FreelanceManager
        fields = ['public', 'interest']

        widgets = {
            'public': CheckboxInput(),
        }

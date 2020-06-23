"""Forms for Freelance Journalists and related functionality."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from freelance.models import (
    FreelanceJournalist,
)


class FreelanceJournalistForm(forms.ModelForm):
    """Form to create or update a Freelance Journalist."""

    class Meta:
        model = FreelanceJournalist
        fields = ['portfolio_link1', 'portfolio_link2', 'portfolio_link3']

        widgets = {
            'portfolio_link1': _TextInput('Portfolio Link 1'),
            'portfolio_link2': _TextInput('Portfolio Link 2'),
            'portfolio_link3': _TextInput('Portfolio Link 3'),
        }


class FreelanceJournalistProfileForm(forms.ModelForm):
    """Form to manage Freelance Journalist profile."""

    class Meta:
        model = FreelanceJournalist
        fields = [
            'public',
            'resume',
            'address',
            'availability',
            'current_location',
            'gear',
            'portfolio_link1',
            'portfolio_link2',
            'portfolio_link3',
        ]

        widgets = {
            'public': CheckboxInput(),
            'address': _TextInput('Mailing Address'),
            'availability': _Textarea('Current Availability', rows=3),
            'current_location': _TextInput('Current Location'),
            'gear': _Textarea('Gear', rows=3),
            'portfolio_link1': _TextInput('Portfolio Link 1'),
            'portfolio_link2': _TextInput('Portfolio Link 2'),
            'portfolio_link3': _TextInput('Portfolio Link 3'),
        }

"""Forms for Freelance Journalists and related functionality."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select, NumberInput

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from freelance.models import (
    FreelanceInvoice,
)


class FreelanceInvoiceForm(forms.ModelForm):
    """Form to create or update a freelance invoice."""

    class Meta:
        model = FreelanceInvoice
        fields = [
            'reference_code',
            'text',
            'total_due',
        ]

        widgets = {
            'reference_code': _TextInput('Reference Code'),
            'text': _Textarea('Details of Invoice', rows=6),
            'total_due': NumberInput(attrs={'class': 'form-control'}),
        }

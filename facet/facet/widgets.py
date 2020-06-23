"""Custom widgets for Facet."""

from django import forms
from django.forms import Textarea, TextInput, CheckboxInput, Select


class ArrayFieldSelectMultiple(forms.SelectMultiple):
    """Allow selecting multiple items."""

    def __init__(self, *args, **kwargs):
        self.delimiter = kwargs.pop('delimiter', ',')
        super(ArrayFieldSelectMultiple, self).__init__(*args, **kwargs)

    def render_options(self, choices, value):
        if isinstance(value, basestring):
            value = value.split(self.delimiter)
        return super(ArrayFieldSelectMultiple, self).render_options(choices, value)


def _TextInput(placeholder=None):
    """Convenience wrapper for TextInput widgets."""

    attrs = {'class': 'form-control'}

    if placeholder:
        attrs['placeholder'] = placeholder

    return TextInput(attrs=attrs)


def _Textarea(placeholder=None, rows=None):
    """Convenience wrapper for Textarea widgets."""

    attrs = {'class': 'form-control'}

    if placeholder:
        attrs['placeholder'] = placeholder

    if rows:
        attrs['rows'] = rows

    return Textarea(attrs=attrs)


def _Select():
    """Convenience wrapper for Select widgets."""

    return Select(attrs={'class': 'form-control'})

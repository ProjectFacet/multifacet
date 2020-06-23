"""Forms for Discussion and related entities."""

from django import forms
from django.forms import Textarea, TextInput

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from communication.models import (
    DirectMessageExchange,
    DirectMessage,
)




class DirectMessageExchangeForm(forms.ModelForm):
    """Create a direct message exchange between two or more participants."""

    def __init__(self, *args, **kwargs):
        participant = kwargs.pop("participant", None)
        super(DirectMessageExchangeForm, self).__init__(*args, **kwargs)

        self.fields['participants'].queryset = entity.get_participant_connections()

    class Meta:
        model = DirectMessageExchange
        fields = ['participants']
        widgets = {
            'participants': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control',
                       'id': 'participants', 'data-placeholder': 'Select Participants'}),
        }


class DirectMessageForm(forms.ModelForm):
    """Create a message in a direct message exchange."""

    class Meta:
        model = DirectMessage
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

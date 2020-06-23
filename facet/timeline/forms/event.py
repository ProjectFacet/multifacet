"""Forms for Eventss and related entities."""

from django import forms
from django.forms import Textarea, TextInput, CheckboxInput, Select
from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from timeline.models import (
    Event,
)

from editorial.models import (
    Project,
    Story,
)

from task.models import (
    Task,
)


class EventForm(forms.ModelForm):
    """ Form to create/edit an event. """

    def __init__(self, *args, **kwargs):
        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        event = kwargs.pop("event", None)
        super(EventForm, self).__init__(*args, **kwargs)

        if event:
            self.fields['team'].queryset = event.get_team_vocab()
        elif entity:
            self.fields['team'].queryset = entity.get_team_vocab()
        elif participant:
            self.fields['team'].queryset = participant.get_team_vocab()

        # set empty labels
        self.fields['event_type'].empty_label = 'Event Type'

    # event_date = forms.DateTimeField(
    #     required=False,
    #     widget=DateTimePicker(
    #         options={'format': 'YYYY-MM-DD HH:mm'},
    #         attrs={'id': 'event_eventdate_picker'}
    #     )
    # )

    class Meta:
        model = Event

        fields = [
            'name',
            'text',
            'team',
            'event_type',
            # 'event_date',
            'venue',
        ]

        widgets = {
            'name': Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Name'}),
            'text': Textarea(attrs={'class': 'form-control', 'id': 'task-text', 'rows': 15,
                                    'placeholder': 'Details'}),
            'team': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control facet-select', 'id': 'event-team',
                       'data-placeholder': 'Team'}),
            'event_type': Select(attrs={'class': 'custom-select', 'id': 'task-status'}),
            'venue': Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Venue'}),
        }

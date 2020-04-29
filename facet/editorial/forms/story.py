"""Forms for Storys and related entities."""

from django import forms
from django.forms import Textarea, TextInput, CheckboxInput, Select

from editorial.models import (
    Story,
)

from editorial.widgets import ArrayFieldSelectMultiple


class StoryForm(forms.ModelForm):
    """Form to create or update a story.

    If there is an entity_owner, partner_with vocabulary comes from entity_owner,
    else the partner_with vocabulary comes from the participant_owner.
    """

    def __init__(self, *args, **kwargs):
        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        story = kwargs.pop("story", None)
        super(StoryForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['partner_with'].queryset = entity.get_partners_vocab()
            self.fields['share_with'].queryset = entity.get_distribution_vocab()
            self.fields['project'].queryset = entity.get_projects_vocab()
        elif participant:
            self.fields['partner_with'].queryset = participant.get_partners_vocab()
            self.fields['share_with'].queryset = participant.get_distribution_vocab()
            self.fields['project'].queryset = participant.get_projects_vocab()

        self.fields['project'].empty_label = 'Optional: Add to Project'

    # embargo_datetime = forms.DateTimeField(
    #     required=False,
    #     widget=DateTimePicker(
    #         options={'format': 'YYYY-MM-DD HH:mm'},
    #         attrs={'id': 'story-embargo-picker'})
    # )
    #
    # share_with_date = forms.DateTimeField(
    #     required=False,
    #     widget=DateTimePicker(
    #         options={'format': 'YYYY-MM-DD HH:mm'},
    #         attrs={'id': 'story-share-picker'})
    # )

    class Meta:
        model = Story
        fields = ['name',
                  'sketch',
                  'project',
                  'collaborate',
                  'partner_with',
                  'embargo',
                  # 'embargo_datetime',
                  'sensitive',
                  'share',
                  'ready_to_share',
                  'share_with',
                  # 'share_with_date',
                  'archived',
                  ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Story Name'}),
            'sketch': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'project': Select(attrs={'class':'mdb-select md-form colorful-select dropdown-ins', 'placeholder': 'Add to Project'}),
            'collaborate': CheckboxInput(),
            'partner_with': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control facet-select',
                       'id': 'partner-with', 'data-placeholder': 'Select Partners'}),
            'embargo': CheckboxInput(),
            'sensitive': CheckboxInput(),
            'share': CheckboxInput(),
            'ready_to_share': CheckboxInput(),
            'share_with': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control facet-select',
                       'id': 'partner-with', 'data-placeholder': 'Select Recipients'}),
            'archived': CheckboxInput(),
        }


class StoryTeamForm(forms.ModelForm):
    """Form to add and edit a story team.

    If there is an entity_owner, team vocabulary comes from entity_owner,
    else the team vocabulary comes from the participant_owner.
    """

    def __init__(self, *args, **kwargs):
        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        story = kwargs.pop("story", None)
        super(StoryTeamForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['team'].queryset = entity.get_team_vocab()
        elif participant:
            self.fields['team'].queryset = participant.get_team_vocab()

    class Meta:
        model = Story
        fields = ['team']
        widgets = {
            'team': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control facet-select',
                       'id': 'story-team', 'data-placeholder': 'Select Story Team'}),
        }

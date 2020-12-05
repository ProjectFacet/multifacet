"""Forms for Projects and related entities."""

from django import forms
from django.forms import Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from editorial.models import (
    Project,
)


class ProjectForm(forms.ModelForm):
    """Form to create or update a project.

    If there is an entity_owner, partner_with vocabulary comes from entity_owner,
    else the partner_with vocabulary comes from the participant_owner.
    """

    def __init__(self, *args, **kwargs):
        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        project = kwargs.pop("project", None)
        super(ProjectForm, self).__init__(*args, **kwargs)

        if entity:
            self.fields['partner_with'].queryset = entity.get_partner_vocab()
        elif participant:
            self.fields['partner_with'].queryset = participant.get_partner_vocab()

    class Meta:
        model = Project
        # fields = ['name', 'desc', 'collaborate', 'partner_with']
        fields = ['name', 'desc', 'collaborate']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'collaborate': CheckboxInput(),
            'partner_with': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control',
                       'id': 'partner-with', 'data-placeholder': 'Select Partners'}),
        }


class ProjectTeamForm(forms.ModelForm):
    """Form to add and edit a project team.

    If there is an entity_owner, team vocabulary comes from entity_owner,
    else the team vocabulary comes from the participant_owner.
    """

    def __init__(self, *args, **kwargs):
        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        project = kwargs.pop("project", None)
        super(ProjectTeamForm, self).__init__(*args, **kwargs)

        if project:
            self.fields['team'].queryset = project.get_team_vocab()
        elif entity:
            self.fields['team'].queryset = entity.get_team_vocab()
        elif participant:
            self.fields['team'].queryset = participant.get_team_vocab()

    class Meta:
        model = Project
        fields = ['team']
        widgets = {
            'team': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control facet-select',
                       'id': 'project-team', 'data-placeholder': 'Select Project Team'}),
        }

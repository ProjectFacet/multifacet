"""Forms for Taskss and related entities."""

from django import forms
from django.forms import Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from task.models import (
    Task,
)


class TaskForm(forms.ModelForm):
    """Form to create/edit a task."""

    def __init__(self, *args, **kwargs):
        entity = kwargs.pop("entity_owner", None)
        participant = kwargs.pop("participant_owner", None)
        task = kwargs.pop("task", None)
        super(TaskForm, self).__init__(*args, **kwargs)

        # TODO future: make assignment team include org users, partner users and collaborators assigned to content
        if task:
            self.fields['team'].queryset = task.get_task_assignment_vocab()
        else:
            self.fields['team'].queryset = org.get_org_users()

        # limit projects and stories to those owned by org or part of content and org is collaborator for
        self.fields['project'].queryset = Project.objects.filter(
            Q(collaborate_with=org) | (Q(organization=org)))
        self.fields['story'].queryset = Story.objects.filter(
            Q(collaborate_with=org) | (Q(organization=org)))
        self.fields['event'].queryset = Event.objects.filter(
            Q(organization=org) | (Q(evt_organization=org)))

        # set empty labels
        self.fields['status'].empty_label = 'Task Status'

    # due_date = forms.DateTimeField(
    #     required=False,
    #     widget=DateTimePicker(
    #         options={'format': 'YYYY-MM-DD HH:mm'},
    #         attrs={'id': 'task_duedate_picker'}
    #     )
    # )

    class Meta:
        model = Task
        fields = [
            'name',
            'text',
            'team',
            'status',
            'important',
            'due_date',
        ]
        widgets = {
            'name': Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Name'}),
            'text': Textarea(attrs={'class': 'form-control', 'id': 'task-text', 'rows': 17,
                                    'placeholder': 'Details'}),
            'team': ArrayFieldSelectMultiple(
                attrs={'class': 'chosen-select form-control task-assign-select',
                       'id': 'task-team', 'data-placeholder': 'Assign to'}),
            'status': Select(attrs={'class': 'custom-select', 'id': 'task-status'}),
            'important': CheckboxInput(attrs={'class': ''}),
            'project': Select(attrs={'class': 'custom-select', 'id': 'task-projects'}),
            'story': Select(attrs={'class': 'custom-select', 'id': 'task-stories'}),
            'event': Select(attrs={'class': 'custom-select', 'id': 'task-events'}),
        }

    class Media:
        css = {'all': ('css/bootstrap-datetimepicker.css', 'css/chosen.min.css')}
        js = ('scripts/chosen.jquery.min.js',)

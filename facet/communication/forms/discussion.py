"""Forms for Discussion and related entities."""

from django import forms
from django.forms import TextInput, Textarea

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from communication.models import (
    Discussion,
    Comment,
)


class DiscussionForm(forms.ModelForm):
    """Create/update discussion channel.

    For all anchors that can associate with a discussion, a default 'main'
    discussion is automatically created when they are.

    All anchors, except items, can have multiple discussion channels.
    """

    class Meta:
        model = Discussion

        fields = ['channel']

        widgets = {
            'channel': TextInput(attrs={'class': 'form-control', 'placeholder': 'Channel Name'}),
        }


class CommentForm(forms.ModelForm):
    """Comment form."""

    class Meta:
        model = Comment

        fields = ['text']

        widgets = {
            'text': Textarea(
                attrs={'id': 'comment-text', 'required': True, 'placeholder': 'Comment',
                       'class': 'form-control', 'rows': 2}
            ),
        }

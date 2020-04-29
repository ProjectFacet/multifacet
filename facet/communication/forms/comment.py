"""Forms for Discussion and related entities."""

from django import forms
from django.forms import Textarea

from communication.models import (
    Comment,
)


class CommentForm(forms.ModelForm):
    """Generic comment form."""

    class Meta:
        model = Comment

        fields = ['text']

        widgets = {
            'text': Textarea(
                attrs={'id': 'comment-text', 'required': True, 'placeholder': 'Comment',
                       'class': 'form-control', 'rows': 2}
            ),
        }

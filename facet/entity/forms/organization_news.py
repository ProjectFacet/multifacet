"""Forms for News Organizations and related functionality."""

from django import forms
from django.forms import Form, Textarea, TextInput, CheckboxInput, Select

from facet.widgets import (
    ArrayFieldSelectMultiple,
    _TextInput,
    _Textarea,
    _Select,
)

from entity.models import (
    NewsOrganization,
)


class NewsOrganizationForm(forms.ModelForm):
    """Form to create or update a News Organization."""

    class Meta:
        model = NewsOrganization
        fields = ['name', 'description', 'location', 'logo', 'cover_photo']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }


class NewsOrganizationProfileForm(forms.ModelForm):
    """Form to manage News Organization profile."""

    class Meta:
        model = NewsOrganization
        fields = [
            'website',
            'mission_statement',
            'list_publicly',
            'display_business_structure',
            'business_structure',
            'display_platforms',
            'platform_print',
            'platform_online',
            'platform_social',
            'platform_network_tv',
            'platform_cable_tv',
            'platform_radio',
            'platform_podcast',
            'platform_newsletter',
            'platform_streaming_video',
            'display_audience',
            'audience',
            'display_ownership',
            'ownership',
            'display_business_model',
            'business_model',
            'display_unionization',
            'unionization',
            'display_diversity',
            'diversity',
            'display_strengths',
            'strengths',
            'display_partner_qualities',
            'partner_qualities',
            'display_best_coverage',
            'best_coverage',
            'display_collab_experience',
            'collab_experience',
            'display_seeking_collabs',
            'seeking_collabs',
            'display_seeking_partners',
            'seeking_partners',
        ]

        widgets = {
            'website': _TextInput('Website'),
            'mission_statement': _Textarea('Mission Statement', rows=3),
            'list_publicly': CheckboxInput(),
            'display_business_structure': CheckboxInput(),
            'business_structure': _TextInput('Business Structure'),
            'display_platforms': CheckboxInput(),
            'platform_print': CheckboxInput(),
            'platform_online': CheckboxInput(),
            'platform_social': CheckboxInput(),
            'platform_network_tv': CheckboxInput(),
            'platform_cable_tv': CheckboxInput(),
            'platform_radio': CheckboxInput(),
            'platform_podcast': CheckboxInput(),
            'platform_newsletter': CheckboxInput(),
            'platform_streaming_video': CheckboxInput(),
            'display_audience': CheckboxInput(),
            'audience': _TextInput('Audience'),
            'display_ownership': CheckboxInput(),
            'ownership': _Textarea('Ownership', rows=3),
            'display_business_model': CheckboxInput(),
            'business_model': _Textarea('Business Model', rows=3),
            'display_unionization': CheckboxInput(),
            'unionization': CheckboxInput(),
            'display_diversity': CheckboxInput(),
            'diversity': _Textarea('Diversity', rows=3),
            'display_strengths': CheckboxInput(),
            'strengths': _Textarea('Strengths', rows=3),
            'display_partner_qualities': CheckboxInput(),
            'partner_qualities': _Textarea('Partner Qualities', rows=3),
            'display_best_coverage': CheckboxInput(),
            'best_coverage': _Textarea('Best Coverage', rows=3),
            'display_collab_experience': CheckboxInput(),
            'collab_experience': _Textarea('Collaboration Experience', rows=3),
            'display_seeking_collabs': CheckboxInput(),
            'seeking_collabs': CheckboxInput(),
            'display_seeking_partners': CheckboxInput(),
            'seeking_partners': CheckboxInput(),
        }

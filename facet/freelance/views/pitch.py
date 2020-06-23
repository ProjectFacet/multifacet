"""Pitch Views for Facet/Freelance.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

# from freelance.forms import ()

from freelance.models import (
    Pitch,
)


class FreelancePitchListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """List of pitches ."""
    pass


class OrganizationPitchListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """List of pitches ."""
    pass


class PitchCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """."""
    pass


class PitchUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """."""
    pass


class PitchDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """."""
    pass


class PitchDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """."""
    pass

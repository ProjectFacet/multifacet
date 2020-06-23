"""Freelance Manager Views for Facet/Freelance."""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import (
    FreelanceManagerForm,
)

from freelance.models import (
    FreelanceManager,
)


class FreelanceManagerCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a freelance manager profile."""

    model = FreelanceManager
    form_class = FreelanceManagerForm
    template_name = 'freelance_manager/freelance_manager_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Profile created."


class FreelanceManagerDashboardView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """Dashboard for manager to view all freelance-related content."""

    template_name = 'freelance_manager/freelance_manager_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        participant = self.request.user

        context['active_assignments'] = []
        context['active_pitches'] = []
        context['active_calls'] = []
        context['active_invoices'] = []
        context['new_comments'] = []

        return context


class FreelanceManagerPublicProfileDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """Publicly viewable profile of a freelance manager."""

    model = FreelanceManager
    template_name = 'freelance_manager/freelance_manager_detail.html'


class FreelanceManagerUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update a freelance manager profile."""

    model = FreelanceManager
    form_class = FreelanceManagerForm
    template_name = 'freelance_manager/freelance_manager_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Profile created."


class FreelanceManagerDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """."""
    pass

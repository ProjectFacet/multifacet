"""FreelanceJournalist Views for Facet/Freelance.

"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import (
    FreelanceJournalistForm,
    FreelanceJournalistProfileForm,
)

from freelance.models import (
    FreelanceJournalist,
)


class FreelanceJournalistCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a Freelance Journalist."""

    model = FreelanceJournalist
    form_class = FreelanceJournalistForm
    template_name = 'freelance_journalist/freelance_journalist_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Profile created."


class FreelanceJournalistDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """View Freelance Journalist profile from perspective of the Freelance Journalist."""

    model = FreelanceJournalist
    template_name = 'freelance_journalist/freelance_journalist_profile.html'

    def notes(self):
        """Return notes."""
        return self.participant.notes.all()

    def internal_images(self):
        """Return internal images."""
        pass

    def internal_documents(self):
        """Return internal documents."""
        pass


class FreelanceJournalistPublicProfileDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """Public Profile for a Freelance Journalist."""

    model = FreelanceJournalist
    template_name = 'freelance_journalist/freelance_journalist_profile.html'


class FreelanceJournalistProfileUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Edit a Freelance Journalist profile."""

    model = FreelanceJournalist
    form_class = FreelanceJournalistProfileForm
    template_name = 'freelance_journalist/freelance_journalist_profile_form.html'

    form_invalid_message = "Something went wrong."
    form_valid_message = "Profile updated."


class FreelanceJournalistDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """."""
    pass

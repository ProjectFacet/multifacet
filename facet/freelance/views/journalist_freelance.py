"""FreelanceJournalist Views for Facet/Freelance.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import ()

from freelance.models import (
    FreelanceJournalist,
)


class FreelanceJournalistCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class FreelanceJournalistDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class FreelanceJournalistPublicProfileDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class FreelanceJournalistUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class FreelanceJournalistDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

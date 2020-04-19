"""StaffJournalist Views for Facet/Staff.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from staff.forms import ()

from staff.models import (
    StaffJournalist,
)


class StaffJournalistCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class StaffJournalistDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class StaffJournalistPublicProfileDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class StaffJournalistUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class StaffJournalistDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class StaffJournalistActivateView():
    """

    """
    pass


class StaffJournalistDeactivateView():
    """

    """
    pass

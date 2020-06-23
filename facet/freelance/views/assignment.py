"""Assignment Views for Facet/Freelance.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

# from freelance.forms import ()

from freelance.models import (
    Assignment,
)


class FreelanceAssignmentListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """."""
    pass


class OrganizationAssignmentListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """."""
    pass


class AssignmentCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """."""
    pass


class AssignmentUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """."""
    pass


class AssignmentDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """."""
    pass


class AssignmentDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """."""
    pass

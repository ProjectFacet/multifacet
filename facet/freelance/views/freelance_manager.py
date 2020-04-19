"""Freelance Manager Views for Facet/Freelance.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import ()

from freelance.models import (
    FreelanceManager,
)


class FreelanceManagerCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class FreelanceManagerDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class FreelanceManagerPublicProfileDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class FreelanceManagerUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class FreelanceManagerDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

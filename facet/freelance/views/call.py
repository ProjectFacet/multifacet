"""Call Views for Facet/Freelance.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import ()

from freelance.models import (
    Call,
)


class CallListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class CallCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class CallUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class CallDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class CallDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass
"""Event Views for Facet/Event.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from event.forms import ()

from event.models import (
    Event,
)


class EventListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class EventCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class EventDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class EventUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class EventDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

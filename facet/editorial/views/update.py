"""Update Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (
    Update,
)


class UpdateListView(FormMessagesMixin, ListView):
    """

    """
    pass


class UpdateCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class UpdateUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class UpdateDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

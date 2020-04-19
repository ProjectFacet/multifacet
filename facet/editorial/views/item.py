"""Item Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (
    Project,
    Story,
)

from communication.models import (
    Discussion,
    Comment,
)


class FacetPreCreateView(FormMessagesMixin, FormView):
    """

    """
    pass


class FacetCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class ItemUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class ItemDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

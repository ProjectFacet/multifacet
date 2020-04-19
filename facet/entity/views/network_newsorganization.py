"""News Organization Network Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from entity.forms import ()

from entity.models import (
    NewsOrganizationNetwork,
)


class NewsOrganizationNetworkListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class NewsOrganizationNetworkCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class NewsOrganizationNetworkUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class NewsOrganizationNetworkDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class NewsOrganizationNetworkStoryListView(LoginRequiredMixin, ListView):
    """

    """
    pass

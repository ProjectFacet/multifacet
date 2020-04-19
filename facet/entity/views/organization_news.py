"""News Organization Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from entity.forms import ()

from entity.models import (
    NewsOrganization,
)


class NewsOrganizationCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class NewsOrganizationUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class NewsOrganizationDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

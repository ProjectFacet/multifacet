"""ContentLicense Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (
    ContentLicense,
)


class ContentLicenseListView(FormMessagesMixin, ListView):
    """

    """
    pass


class ContentLicenseCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class ContentLicenseUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class ContentLicenseDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

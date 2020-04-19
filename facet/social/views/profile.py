"""Platform Profile Views for Facet/Social.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from social.forms import ()

from social.models import (
    PlatformProfile,
    Website,
)


class PlatformProfileListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class PlatformProfileCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class PlatformProfileUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class PlatformProfileDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# Website

class WebsiteListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class WebsiteCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class WebsiteUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class WebsiteDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

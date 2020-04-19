"""Simple Asset Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (

)

# Simple Asset Library

class SimpleAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class SimpleImageAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class SimpleDocumentAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class SimpleAudioAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class SimpleVideoAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


# Simple Image Views

class SimpleImageCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class SimpleImageLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class SimpleImageUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class SimpleImageAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class SimpleImageAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Document Views

class SimpleDocumentCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class SimpleDocumentUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class SimpleDocumentAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class SimpleDocumentLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class SimpleDocumentAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Audio Views

class SimpleAudioCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class SimpleAudioUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class SimpleAudioAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class SimpleAudioLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class SimpleAudioAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Video Views

class SimpleVideoCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class SimpleVideoUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class SimpleVideoAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class SimpleVideoLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class SimpleVideoAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass

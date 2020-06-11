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


class InternalImageAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class InternalDocumentAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class InternalAudioAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class InternalVideoAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


# Simple Image Views

class InternalImageCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class InternalImageLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalImageUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalImageAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class InternalImageAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Document Views

class InternalDocumentCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class InternalDocumentUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalDocumentAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class InternalDocumentLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalDocumentAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Audio Views

class InternalAudioCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class InternalAudioUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalAudioAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class InternalAudioLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalAudioAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Video Views

class InternalVideoCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class InternalVideoUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class InternalVideoAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class InternalVideoLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalVideoAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass

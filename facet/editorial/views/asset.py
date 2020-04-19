"""Asset Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (

)


# Library Views

class AssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class ImageAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class DocumentAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class AudioAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class VideoAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


# Image Asset Views

class ImageAssetCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class LibraryImageAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class ImageAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


class ImageAssetUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class ImageAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# Document Asset Views

class DocumentAssetCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class LibraryDocumentAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class DocumentAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


class DocumentAssetUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class DocumentAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# Audio Asset Views

class AudioAssetCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class LibraryAudioAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class AudioAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


class AudioAssetUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class AudioAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# Video Asset Views

class VideoAssetCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class LibraryVideoAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class VideoAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


class VideoAssetUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class VideoAssetDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

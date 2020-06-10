"""Asset Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import (
    ImageAssetForm, LibraryImageAssociateForm, SimpleImageForm, SimpleImageLibraryAssociateForm,
    DocumentAssetForm, LibraryDocumentAssociateForm, SimpleDocumentForm, SimpleDocumentLibraryAssociateForm,
    AudioAssetForm, LibraryAudioAssociateForm, SimpleAudioForm, SimpleAudioLibraryAssociateForm,
    VideoAssetForm, LibraryVideoAssociateForm, SimpleVideoForm, SimpleVideoLibraryAssociateForm,
)

from editorial.models import (
    Project, Story, Item,
    ImageAsset, DocumentAsset, AudioAsset, VideoAsset,
    SimpleImage, SimpleDocument, SimpleAudio, SimpleVideo,
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


# Simple Asset Library Views

# ACCESS: Only an org's users should be able to see an organization's internal asset library
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

# Simple Image

# ACCESS: Any org user, or user from an organization that is in collaborate_with
# should be able to create a simple asset for P, Sr, St, F
# Contractors should only be able to do so for PSSF that they have access to
# That should be handled by limiting which PSSF they have access to.
class SimpleImageCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
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


# Simple Document
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


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class SimpleDocumentLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class SimpleDocumentAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Audio
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


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class SimpleAudioLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class SimpleAudioAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass


# Simple Video
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


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class SimpleVideoLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class SimpleVideoAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass

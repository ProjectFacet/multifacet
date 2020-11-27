"""Library Views for Facet/Internalasset.
"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from internalasset.forms import (
    InternalImageForm, InternalImageLibraryAssociateForm,
    InternalDocumentForm, InternalDocumentLibraryAssociateForm,
    InternalAudioForm, InternalAudioLibraryAssociateForm,
    InternalVideoForm, InternalVideoLibraryAssociateForm,
)

from editorial.models import (
    Project, Story, Item,
)

from internalasset.models import (
    InternalImage, InternalDocument, InternalAudio, InternalVideo,
)


# ACCESS: Only an org's users should be able to see an organization's internal asset library
class InternalAssetLibraryTemplateView(LoginRequiredMixin, TemplateView):
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

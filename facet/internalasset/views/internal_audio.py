"""Views for Facet/Internalasset.
"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from internalasset.forms import (
    InternalAudioForm,
    InternalAudioLibraryAssociateForm,
)

from editorial.models import (
    Project, Story, Item,
)

from internalasset.models import InternalAudio


# Internal Audio
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


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
class InternalAudioLibraryAssociateView(LoginRequiredMixin, FormView):
    """

    """
    pass


class InternalAudioAssetDisassociateView(LoginRequiredMixin, View):
    """

    """
    pass

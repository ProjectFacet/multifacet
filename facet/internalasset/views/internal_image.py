"""Views for Facet/Internalasset.
"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from internalasset.forms import (
    InternalImageForm, InternalImageLibraryAssociateForm,
)

from editorial.models import (
    Project, Story, Item,
)

from internalasset.models import InternalImage


# Internal Image

# ACCESS: Any org user, or user from an organization that is in collaborate_with
# should be able to create a internal asset for P, Sr, St, F
# Contractors should only be able to do so for PSSF that they have access to
# That should be handled by limiting which PSSF they have access to.
class InternalImageCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


# ACCESS: Any org user should be able to add an asset for a P, Sr, St, F
# A user from an organization that is in collaborate_with or
# contractors should not be able to do this because doing so requires access to
# an org's entire asset library.
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

"""Correction Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (
    Correction,
)


class CorrectionListView(FormMessagesMixin, ListView):
    """

    """
    pass


class CorrectionCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class CorrectionUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class CorrectionDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

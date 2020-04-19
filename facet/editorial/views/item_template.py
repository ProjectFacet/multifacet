"""Item Template Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (

)


class ItemTemplateCreateView(LoginRequiredMixin, CreateView):
    """

    """
    pass


class ItemTemplateUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class ItemTemplateListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class ItemTemplateDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class ItemTemplateDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

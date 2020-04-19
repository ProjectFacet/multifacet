"""Invoice Views for Facet/Freelance.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import ()

from freelance.models import (
    Invoice,
)


class InvoiceListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class InvoiceCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class InvoiceUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class InvoiceDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class InvoiceDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

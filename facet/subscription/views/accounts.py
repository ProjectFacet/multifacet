"""Account Subscription Views for Facet/Subscription.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from subscription.forms import ()

from subscription.models import ()


class AccountSelectionView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class OrganizationSubscriptionUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass


class ContractorSubscriptionUpdateView(LoginRequiredMixin, UpdateView):
    """

    """
    pass

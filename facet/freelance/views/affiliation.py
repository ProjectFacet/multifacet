"""Affiliation Views for Facet/Freelance.

FreelancerAffiliationRecord:
    Information tracked by a news organization about freelancers.

    Basic info like email, bio, skillset, availability, current_location, gear
    are available on FreelanceJournalist.

    The data captured is for a News Organization's internal
    notes regarding their affiliation with a Freelance Journalist.

OrganizationAffiliationRecord:
    Information tracked about an organization by a freelancer.

    The data captured is for a freelancer's records regarding
    their affiliation with a NewsOrganization.

"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from freelance.forms import ()

from freelance.models import (
    FreelanceJournalist,
    FreelancerAffiliationRecord,
    OrganizationAffiliationRecord
)

# Freelancer Affiliation Record Views

class FreelancerAffiliationRecordCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class FreelancerAffiliationRecordDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class FreelancerAffiliationRecordUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class FreelancerAffiliationRecordDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


# Organization Affiliation Record Views

class OrganizationAffiliationRecordCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class OrganizationAffiliationRecordDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class OrganizationAffiliationRecordUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class OrganizationAffiliationRecordDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

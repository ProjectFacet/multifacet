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

# from freelance.forms import ()

from freelance.models import (
    FreelancerAffiliationRecord,
    OrganizationAffiliationRecord
)

from participant.models import (
    FreelanceJournalist,
)

# Freelancer Affiliation Record Views

class FreelancerAffiliationRecordCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a record for an organization regarding details of a freelancer they are working with.

    An affiliation record can be created:
    - automatically by creating an assignment
    - manually by clicking a button to create a record (if one does not already exist)
    """




class FreelancerAffiliationRecordDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """Display record."""
    pass


class FreelancerAffiliationRecordUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update a record."""
    pass


class FreelancerAffiliationRecordDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Delete a record."""
    pass


# Organization Affiliation Record Views

class OrganizationAffiliationRecordCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a record for a freelance journalist regarding details of an organization they are working with.."""
    pass


class OrganizationAffiliationRecordDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """Display record."""
    pass


class OrganizationAffiliationRecordUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update a record."""
    pass


class OrganizationAffiliationRecordDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Delete a record."""
    pass

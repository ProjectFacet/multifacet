from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, CreateView, View, TemplateView

# import models

# import forms

# Index page of entire app projectfacet.com/
class LandingTemplateView(TemplateView):
    """Landing page explaining Project Facet and guiding users to scenario
    that is appropriate for their goals."""

    template_name = 'landing.html'


class DashboardDeterminationView(LoginRequiredMixin, TemplateView):
    """After login, determine user profile status and redirect to appropriate
    dashboard.

    Dashboards for users who've not yet been approved are below.
    Dashboards for verified profile types are handled in the appropriate app.

    StaffJournalistDashboardView: staff/views/journalist_staff_dashboard.py
    FreelanceJournalistDashboardView: freelance/views/journalist_freelance_dashboard.py
    """

    def get(self, request, *args, **kwargs):

        participant = self.request.user

        if participant.staffjournalist:
            return redirect('staff:dashboard_staff')
        elif participant.freelancejournalist:
            return redirect('freelance:dashboard_freelance')
        else:
            return redirect('dashboard_account_requested')


class PreAccountApprovalDashboardView(LoginRequiredMixin, TemplateView):
    """Displays dashboard and details about Facet for user who has requested an
    account but has not yet been approved."""

    template_name = 'preapproved_dashboard.html'

    def get_context_data(self):
        participant = self.request.user

        content = []

        return context

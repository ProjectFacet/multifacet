from django.shortcuts import render

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


# ACCESS: All logged in users have access to dashboard
class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    """ Returns participant's unique dashboard.

    A freelancer gets their freelance dashboard.
    - active assignments
    - active pitches (all status except complete)
    - active calls
    - active invoices
    - new comments since last login

    A staff journalist gets their staff dashboard.
    - newsorganization
    - their projects, stories
    - new stories associated with the organization (top 10 since last login)
    - stories associated with organization running today
    - tasks with upcoming due dates
    - events with upcoming dates they are associated with
    """

    template_name = 'dashboard.html'

    def get_context_data(self):
        participant = self.request.user

        # If participant has a Staff Journalist profile
        if participant.staffjournalist:
            org = participant.staffjournalist.newsorganization
            current_projects = []
            current_stories = []
            new_org_stories = []
            running_org_stories = []
            upcoming_tasks = []
            upcoming_events = []

        # If Participant has a Freelance profile
        if participant.freelancejournalist:
            active_assignments = []
            active_pitches = []
            active_calls = []
            active_invoices = []
            new_comments = []

        return context

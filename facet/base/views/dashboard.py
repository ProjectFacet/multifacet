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
    A staff journalist will see their staff dashboard.
    """

    template_name = 'dashboard.html'

    def get_context_data(self):
        participant = self.request.user

        #If participant has a Staff Journalist profile
        # if participant.staffjournalist:
        #     org = participant.staffjournalist.newsorganization



        # If Participant has a Freelance profile

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, CreateView, View, TemplateView

# import models


# import forms


class StaffJournalistDashboardView(LoginRequiredMixin, TemplateView):
    """Displays dashboard for a staff journalist.

    A staff journalist gets:
    - newsorganization
    - their projects, stories
    - new stories associated with the organization (top 10 since last login)
    - stories associated with organization running today
    - tasks with upcoming due dates
    - events with upcoming dates they are associated with


    """

    template_name = 'journalist_staff_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        participant = self.request.user

        org = participant.staffjournalist.newsorganization
        context['current_projects'] = []
        context['current_stories'] = []
        context['new_org_stories'] = []
        context['running_org_stories'] = []
        context['upcoming_tasks'] = []
        context['upcoming_events'] = []

        return context

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, CreateView, View, TemplateView

# import models
from freelance.models import (
    FreelanceJournalist,
    FreelanceManager,
    Call,
    Pitch,
    Assignment,
    FreelanceInvoice,
)

from freelance.forms import (
    FreelanceJournalistForm,
)


class FreelanceJournalistDashboardView(LoginRequiredMixin, TemplateView):
    """Displays dashboard for a freelance journalist.

    A freelancer gets:
    - active assignments
    - active pitches (all status except complete)
    - active calls
    - active invoices
    - new comments since last login
    """

    template_name = 'freelance_journalist_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        participant = self.request.user

        context['active_assignments'] = []
        context['active_pitches'] = []
        context['active_calls'] = []
        context['active_invoices'] = []
        context['new_comments'] = []

        return context

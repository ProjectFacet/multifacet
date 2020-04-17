from django.shortcuts import render

from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, CreateView, View, TemplateView

# import models


# import forms





#----------------------------------------------------------------------#
#   Initial View
#----------------------------------------------------------------------#

# This is the only general view that does not require login
class LandingTemplateView(TemplateView):
    """Return static homepage for pre-login users."""

    template_name = 'base/landing.html'


#----------------------------------------------------------------------#
#   Dashboard View
#----------------------------------------------------------------------#

# ACCESS: All users have access to dashboard
class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    """ Returns participant's unique dashboard."""

    template_name = 'base/dashboard.html'

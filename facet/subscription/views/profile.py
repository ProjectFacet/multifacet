from django.shortcuts import render

from braces.views import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, CreateView, View, TemplateView

# import models


# import forms





class ProfileSelectionTemplateView(LoginRequiredMixin, TemplateView):
    """Account type selection page."""

    template_name = 'profile_select.html'

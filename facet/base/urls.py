from django.urls import path

from .views import (
    dashboard,
)


app_name = 'base'
urlpatterns = [
    # ex: /polls/
    path('', dashboard.LandingTemplateView.as_view(), name='landing'),
    path('/dashboard', dashboard.DashboardTemplateView.as_view(), name='dashboard'),
]

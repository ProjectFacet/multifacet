from django.urls import path

from .views import (
    dashboard,
)


app_name = 'base'
urlpatterns = [
    path('', dashboard.LandingTemplateView.as_view(), name='landing'),
    path('dashboard/', dashboard.DashboardDeterminationView.as_view(), name='dashboard'),
    path('dashboard/account-requested/', dashboard.PreAccountApprovalDashboardView.as_view(), name='dashboard_account_requested'),
]

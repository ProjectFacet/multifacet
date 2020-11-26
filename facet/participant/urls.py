from django.urls import path

from .views import (
    journalist_staff_dashboard,
)


app_name = 'participant'
urlpatterns = [
    # ex: /polls/
    path('dashboard/', journalist_staff_dashboard.StaffJournalistDashboardView.as_view(), name='dashboard_staff'),
]

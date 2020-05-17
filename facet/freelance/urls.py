from django.urls import path

from .views import (
    journalist_freelance_dashboard,
)


app_name = 'freelance'
urlpatterns = [
    # ex: /polls/
    path('dashboard/', journalist_freelance_dashboard.FreelanceJournalistDashboardView.as_view(), name='dashboard_freelance'),
]

from django.urls import path

from .views import (
    profile,
)

app_name = 'subscription'
urlpatterns = [
    #Subscription
    path('profile/select/', profile.ProfileSelectionTemplateView.as_view(), name='profile_select'),
]

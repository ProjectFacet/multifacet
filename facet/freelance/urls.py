from django.urls import path

from . import views

urlpatterns = [
    path('', views.freelance, name='freelance'),
]

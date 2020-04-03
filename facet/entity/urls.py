from django.urls import path

from . import views

urlpatterns = [
    path('', views.entity, name='entity'),
]

"""Task Views for Facet/Task.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from task.forms import ()

from task.models import (
    Task,
)


class TaskListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class TaskCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class TaskDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass


class TaskUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class TaskDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

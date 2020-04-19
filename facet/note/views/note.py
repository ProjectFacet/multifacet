"""Note Views for Facet/Note.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from note.forms import ()

from note.models import (
    Note,
)


class NoteListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """

    """
    pass


class NoteCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """

    """
    pass


class NoteUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class NoteDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass

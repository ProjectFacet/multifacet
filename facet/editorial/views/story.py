"""Story Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import ()

from editorial.models import (
    Project,
    Story,
)

from communication.models import (
    Discussion,
    Comment,
)

class StoryListView(ListView):
    """

    """
    pass


class StoryCreateView(FormMessagesMixin, CreateView):
    """

    """
    pass


class StoryUpdateView(FormMessagesMixin, UpdateView):
    """

    """
    pass


class StoryDetailView(DetailView):
    """

    """
    pass


class StoryTeamUpdateView(FormMessagesMixin, UpdateView):
    """

    """
    pass


class StoryDeleteView(FormMessagesMixin, DeleteView):
    """

    """
    pass


class StoryScheduleView(View):
    """

    """
    pass

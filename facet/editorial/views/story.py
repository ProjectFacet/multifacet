"""Story Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import (
    StoryForm,
    StoryTeamForm,
)

from editorial.models import (
    Project,
    Story,
)

from communication.models import (
    Discussion,
    Comment,
)

class StoryCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """A logged in user with the appropriate permissions can create a story.

    Stories can have items, assets, notes, discussions,
    simple assets, calendar objects and meta information.
    """

    model = Story
    template_name = 'story/story_form.html'
    form_class = StoryForm

    form_invalid_message = "Something went wrong."
    form_valid_message = "Story created."

    def form_valid(self, form):
        """Save -- but first adding participant_owner and entity_owner if applicable."""

        self.object = form.save(commit=False)
        participant = self.request.user
        self.object.participant_owner = participant
        if participant.staffjournalist:
            entity = participant.staffjournalist.newsorganization
            self.object.entity_owner = entity
        self.object.save()
        return redirect(self.object)


class StoryDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass
    # model = Story
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['x'] = 'x'
    #     return context


class StoryUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class StoryDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class StoryListView(LoginRequiredMixin, ListView):
    """Displays a filterable table of stories.

    Initial display organizes listings by creation date."""

    pass
    # model = Story
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['x'] = 'x'
    #     return context

class StoryTeamUpdateView(FormMessagesMixin, UpdateView):
    """

    """
    pass




class StoryStoryView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class StoryAssetView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class StoryTaskView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class StoryNoteView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class StoryScheduleView(LoginRequiredMixin, FormMessagesMixin, TemplateView):
    """

    """
    pass

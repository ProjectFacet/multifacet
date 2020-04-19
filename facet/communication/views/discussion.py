""" Manages Discussion and Comments.

A Discussion with channel = "Main" is automatically created for:
Entity, Project, Story, Item, Task, Event, Pitch, Assignment

Additional Discussions with custom channel names can be created for:
Entity, Project
Ex. A NewsOrganization can have multiple Discussion/Channels

"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView , UpdateView, DetailView, CreateView, View
from braces.views import LoginRequiredMixin

# from communication.forms import (
#
#     )

from communication.models import (
        Discussion,
        Comment,
    )


class DiscussionCreateView(CreateView):
    """Create a Discussion with a channel != 'main'."""

    model = Discussion
    template_name = 'discussion_form.html'
    fields = ['channel', 'anchor']


class DiscussionUpdateView(UpdateView):
    """Change channel name for a Discussion."""

    model = Discussion
    template_name = 'discussion_form.html'
    fields = ['channel']


class DiscussionDeleteView(DeleteView):
    """Delete a discussion/channel."""
    pass


class CommentCreateView(CreateView):
    """Create a Comment associated with a Discussion."""

    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        """Save -- but first add some information."""

        self.object = comment = form.save(commit=False)
        # set request based attributes
        comment.participant = self.request.user
        # association with entity or content is handled on the discussion
        discussion_id = self.request.POST.get('discussion')
        comment.discussion = get_object_or_404(Discussion, id=discussion)
        comment.text = self.request.POST.get('text')
        comment.save()
        # TODO record action for notifications
        # TODO return user to location of Comment's parent Discussion
        return HttpResponseRedirect(reverse)


class CommmentUpdateView(UpdateView):
    """Change channel name for a Discussion."""

    pass
    # model = Comment
    # template_name = 'comment_form.html'
    # fields = ['text']

    #TODO add updated, edited (boolean) to Comment model

class DiscussionDeleteView(DeleteView):
    """Delete a discussion/channel."""
    pass

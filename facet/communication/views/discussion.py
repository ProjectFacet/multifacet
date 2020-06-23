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

from communication.forms import (
        DiscussionForm,
        CommentForm,
    )

from communication.models import (
        Discussion,
        Comment,
    )


class DiscussionCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a Discussion with a channel != 'main'."""

    model = Discussion
    template_name = 'discussion_form.html'
    form_class = DiscussionForm

    form_invalid_message = "Something went wrong."
    form_valid_message = "Discussion created."

    def form_valid(self, form):
        """Save -- but first adding anchor."""

        self.object = discussion = form.save(commit=False)
        anchor_id = form.cleaned_data['anchor']
        anchor = get_object_or_404(Anchor, id=anchor_id)
        discussion.anchor = anchor
        discussion.channel = form.cleaned_data['channel']
        discussion.save()
        return redirect(self.object)


class DiscussionUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Change channel name for a Discussion."""

    model = Discussion
    template_name = 'discussion_form.html'
    fields = ['channel']


class DiscussionDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Delete a non 'main' discussion/channel from a Entity or Project."""

    model = Discussion
    template_name = "discussion_delete.html'"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post-deletion, return to the discussion anchor."""

        anchor = self,request.Post.get('anchor')
        if anchor.entity:
            return anchor.entity.get_absolute_url()
        if anchor.project:
            return anchor.project.get_absolute_url()


class CommentCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
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
        discussion = Discussion.objects.get(id=discussion_id)
        comment.discussion = discussion
        comment.text = self.request.POST.get('text')
        comment.save()
        # TODO record action for notifications
        # return user to location of Comment's parent Discussion
        return discussion.anchor.get_absolute_url()


class CommmentUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Edit a comment in a discussion."""

    pass
    # model = Comment
    # template_name = 'comment_form.html'
    # fields = ['text']

    #TODO add updated, edited (boolean) to Comment model

class CommentDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Delete a comment."""
    pass

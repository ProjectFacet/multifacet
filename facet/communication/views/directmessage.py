""" Manages Direct Messaging.

"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView , UpdateView, DetailView, CreateView, View
from braces.views import LoginRequiredMixin

from communication.forms import (
        DirectMessageExchange,
        DirectMessage,
    )

from communication.models import (
        DirectMessageExchange,
        DirectMessage,
    )


class DirectMessageExchangeCreateView(CreateView):
    """Create a direct message exchange among 2 or more participants."""

    model DirectMessageExchange
    template_name = 'directmessage_exchange_form.html'
    form_class = DirectMessageExchangeForm

    form_invalid_message = "Something went wrong."
    form_valid_message = "Group chat created."

    def form_valid(self, form):
        """Save -- but first add."""

        self.object = directmessage_exchange = form.save(commit=False)
        anchor_id = form.cleaned_data['anchor']
        anchor = Anchor.objects.get(id=anchor_id)
        participants = form.cleaned_data['participants']
        discussion.anchor = anchor
        discussion.save()
        discussion.participants.add(*participants)
        return redirect(self.object)


class DirectMessageCreateView(CreateView):
    """Create a direct message for a direct message exchange."""

    model = DirectMessage
    form_class = DirectMessageForm

    def form_valid(self, form):
        """Save -- but first add some information."""

        self.object = comment = form.save(commit=False)
        # set request based attributes
        directmessage.author = self.request.user
        # association with entity or content is handled on the discussion
        dm_exchange_id = self.request.POST.get('dm_exchange')
        dm_exchange = DirectMessageExchange.objects.get(id=dm_exchange_id)
        directmessage.dm_exchange = dm_exchange
        directmessage.text = self.request.POST.get('text')
        directmessage.save()
        # TODO record action for notifications
        # return user to location of Comment's parent Discussion
        return directmessage_exchange.anchor.get_absolute_url()


class DirectMessageUpdateView(UpdateView):
    """Update a direct message."""

    pass
    # model = DirectMessage
    # template_name = 'directmessage_form.html'
    # fields = ['text']


class DirectMessageDeleteView(DeleteView):
    """Delete a direct message."""
    pass

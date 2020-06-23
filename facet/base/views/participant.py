from django.shortcuts import render

from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, CreateView, View, DeleteView

# import models


# import forms


# A Participant is created:
# - through django all auth account-signup
# - TODO: after being invited by an organization, project, story

class ParticipantUpdateView(LoginRequiredMixin, UpdateView):
    """Update a Participant profile."""

    model = Participant
    # TODO create ParticipantProfileForm
    # form_class = ParticipantProfileForm
    template_name = 'base/templates/participant_profile_form.html'

    def form_valid(self, form):
        """Update values for a Participant."""

    def get_success_url(self):
        """Record action for activity stream."""

        return super(ParticipantUpdateView, self).get_success_url()


class ParticipantDetailView(LoginRequiredMixin, DetailView):
    """The private profile for a Participant.

    Displays the Participant's information and associations as StaffJournalist,
    FreelanceJournalist or other.

    Visible only to the Participant.
    Public Profiles are managed in their respective apps.

    StaffJournalist profile visible to Organizations, Partners:
        staff/views/

    FreelanceJournalist profile visible to FreelanceManagers, Organizations, etc:
        freelance/views/
    """

    model = Participant
    template_name = 'base/templates/participant_detail.html'

    def notes(self):
        """Get all notes associated with participant and form for creating notes."""

        notes = self.object.note_set.all().order_by('-creation_date')
        form = NoteForm()

        return {'notes': notes, 'form': form}

    def tasks(self):
        """Get all tasks associated with a Participant."""

        pass
        # TODO write model method to retrieve sorted tasks


class ParticipantDeleteView(LoginRequiredMixin, DeleteView):
    """The deletion of a profile for a Participant.

    While a Participant can delete their profile from Facet as they would wish
    do so in order to delete their account or remove themselves from the platform.

    For the purposes of attribution, any content associated with them, but owned
    by another entity, those attributions must remain and will be recorded as
    their credit_name in plain text in place of a link to their profile on the platform.
    """

    model = Participant
    template_name = 'base/templates/participant_delete.html'

    # TODO added necessary model fields to facilitate plain-text recording of an
    # attribution of a participant who has deleted their profile.

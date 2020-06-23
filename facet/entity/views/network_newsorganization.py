"""News Organization Network Views for Facet/Editorial.


"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from entity.forms import (
    NewsOrganizationNetworkForm,
)

from entity.models import (
    NewsOrganization,
    NewsOrganizationNetwork,
)


class NewsOrganizationNetworkCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a news organization network."""

    model = NewsOrganizationNetwork
    form_class = NewsOrganizationNetworkForm
    template_name = 'network_newsorganization_form.html'

    def form_valid(self, form):
        """Save, but first set details."""

        self.object = neworganizationnetwork = form.save(commit=False)
        newsorganizationnetwork.participant_owner = self.request.user
        if self.request.user.staffjournalist:
            newsorganizationnetwork.entity_owner = self.request.user.staffjournalist.newsorganization.entity_owner_profile
        newsorganizationnetwork.save()
        return redirect(newsorganizationnetwork)


class NewsOrganizationNetworkDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """Manage news organization network dashboard."""

    """The primary dashboard for a NewsOrganization."""

    model = NewsOrganizationNetwork
    template_name = 'network_newsorganization_dashboard.html'

    def test_user(self, user):
        """User must be affiliated with this news organization network to view the dashboard."""

        self.object = self.get_object()
        if user.staffjournalist.newsorganization.network_member_profile == self.object.members:
            return True
        elif user.network_member_profile = self.object.members:
            return True

        raise PermissionDenied()

    def discussions(self):
        """Return network discussions."""
        pass

    def notes(self):
        """Return network notes."""
        pass

    def internal_images(self):
        """Return internal images."""
        pass

    def internal_documents(self):
        """Return internal documents."""
        pass


class NewsOrganizationNetworkUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update meta information about a news organization network."""

    model = NewsOrganizationNetwork
    form_class = 'NewsOrganizationNetworkForm'
    template_name = 'network_newsorganization_form.html'

    def test_user(self, user):
        """User must be affiliated with this news organization network to view the dashboard."""

        self.object = self.get_object()
        if user.staffjournalist.newsorganization.entity_owner_profile == self.object.entity_owner:
            return True
        elif user == self.object.participant_owner:
            return True

        raise PermissionDenied()

class NewsOrganizationNetworkDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Manage the deletion of a news organization network."""

    def test_user(self, user):
        """User must be affiliated with this news organization network to view the dashboard."""

        self.object = self.get_object()
        if user.staffjournalist.newsorganization.entity_owner_profile == self.object.entity_owner:
            return True
        elif user == self.object.participant_owner:
            return True

        raise PermissionDenied()

    def get_success_url(self):
        """Post deletion, return to list of networks."""

        return reverse('network_newsorganization_list')


class NewsOrganizationNetworkListView(LoginRequiredMixin, FormMessagesMixin, ListView):
    """List networks that a newsorganization is either an owner or member of."""

    def get_context_data(self, **kwargs):
        """Retrieve networks based on user, newsorganization."""

        newsorganization_id = self.kwargs['pk']
        newsorganization = NewsOrganization.objects.get(id=newsorganization_id)
        context['networks'] = NewsOrganization.get_networks(newsorganization)
        return context


class NewsOrganizationNetworkStoryListView(LoginRequiredMixin, ListView):
    """ Displays a filterable table of stories marked as shared/ready to share by any
    members of a network for that network.

    Initial display organizes content by story>item>est. run date
    Filterable by story name, item type, item name, due for edit, est. run date, credit,
    editor, status.

    Stories marked as share appear but are greyed out/inaccessible until the owner marks
    them as Ready to Share. (This is so partners know it will exist and can plan to incorporate
    it once it becomes available.)
    """

    context_object_name = 'networkstories'
    template_name = 'network_newsorganization_story_list.html'

    def get_context_data(self, **kwargs):
        """Return stories."""

        network = NewsOrganizationNetwork.objects.get(id=self.kwargs['pk'])
        if network.participant_owner:
            participant_owner = network.participant_owner
        if network.entity_owner:
            entity_owner = network.entity_owner

        # get stories shared with network
        stories = NewsOrganizationNetwork.get_network_shared_stories(network)
        # create unique list of stories
        shared_networkstories = [story for story in shared_networkstories if story.organization != organization]
        networkstories = set(shared_networkstories)
        # get list of stories entity has copied or participant has copied
        if self.request.user.staffjournalist:
            copied_content = self.request.user.staffjournalist.newsorganization.get_copied_content()
        else:
            copied_content = self.request.user.get_copied_content()
        # temp attribute showing whether the story has already been picked up
        for story in stories:
            if story in copied_content:
                story.already_picked_up=True
            else:
                story.already_picked_up=False
        # return stories
        return networkstories


# TODO
class NewsOrganizationNetworkInvitationOfferView():
    """Invite a member to the network."""
    pass

# TODO
class NewsOrganizationNetworkInvitationResponseView():
    """Process an accepted or declined invitation."""
    pass

# TODO
class NewsOrganizationNetworkJoinRequestView():
    """Request to join a network."""
    pass

# TODO
class NewsOrganizationNetworkJoinResponseView():
    """Accept or decline join requests."""
    pass

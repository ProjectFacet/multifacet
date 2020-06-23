"""News Organization Views for Facet/Editorial.


"""

from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from entity.forms import (
    NewsOrganizationForm,
)

from entity.models import (
    NewsOrganization,
)


class NewsOrganizationCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """Create a new NewsOrganization."""

    model = NewsOrganization
    form_class = NewsOrganizationForm
    template_name = 'newsorganization_form.html'

    def form_valid(self, form):
        """Save, but first set owner of newsorganization to user creating it."""

        self.object = newsorganization = form.save(commit=False)
        newsorganization.participant_owner = self.request.user
        newsorganization.save()
        return redirect(self.object)


class NewsOrganizationDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """The primary dashboard for a NewsOrganization."""

    model = NewsOrganization
    template_name = 'newsorganization_dashboard.html'

    def test_user(self, user):
        """User must be affiliated with this news organization to view the dashboard."""

        self.object = self.get_object()
        if user.staffjournalist.newsorganization == self.object:
            return True

        raise PermissionDenied()

    def discussions(self):
        """Return organization discussions."""
        pass

    def notes(self):
        """Return organization notes."""
        pass

    def internal_images(self):
        """Return internal images."""
        pass

    def internal_documents(self):
        """Return internal documents."""
        pass


class NewsOrganizationUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update the basic information of a NewsOrganization."""

    model = NewsOrganization
    form_class = NewsOrganizationForm
    template_name = 'newsorganization_form.html'

    def test_user(self, user):
        """User must be affiliated with this news organization to view the dashboard."""

        self.object = self.get_object()
        if user.staffjournalist.newsorganization == self.object:
            return True

        raise PermissionDenied()

    def get_context_data(self, **kwargs):
        """Include team."""

        context = super(NewsOrganizationUpdateView, self).get_context_data(**kwargs)
        context['staff_team'] = self.object.get_staff_team()
        return context


class NewsOrganizationProfileDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """View the public profile information of a NewsOrganization."""

    model = NewsOrganization
    template_name = 'newsorganization_public_profile.html'


class NewsOrganizationProfileUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """Update the profile information of a NewsOrganization."""

    model = NewsOrganization
    form_class = NewsOrganizationProfileForm
    template_name = 'newsorganization_profile_form.html'

    def test_user(self, user):
        """User must be affiliated with this news organization to view the dashboard."""

        self.object = self.get_object()
        if user.staffjournalist.newsorganization == self.object:
            return True

        raise PermissionDenied()


#TK Manage deletion such that legacy links like original ownership of partner content is maintained
class NewsOrganizationDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """Delete a news organization from Facet."""
    pass

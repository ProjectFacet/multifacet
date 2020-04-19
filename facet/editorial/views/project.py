"""Project Views for Facet/Editorial.

A Project is a group of stories.

ProjectListView: List of projects appropriate for context.
    - A StaffJournalist would see:
        /<newsorg slug>/projects: all projects owned by their NewsOrganization
        /<newsorg network slug>/projects: all projects owned by or partnered with
                                          NewsOrganizationNetwork
    - A FreelanceJournalist would see:
        /dashboard/projects: all projects they are included in as a partner
ProjectCreateView: View that handles creating a new Project
ProjectUpdateView: View that handles updating a Project's attributes
ProjectTeamUpdateView: View to edit a Project's team
ProjectDeleteView: View to delete a Project. A project can be deleted by Participant
    who created it or by an admin of the entity the project is associated with.
ProjectDetailView: View that presents all of the details and associations for a Project
ProjectAssetTemplateView: Presents asset library of a Project
ProjectStoryListTemplateView: Presents list of stories associated with a Project

"""

from django.shortcuts import render
from braces.views import LoginRequiredMixin, FormMessagesMixin
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


class ProjectListView(LoginRequiredMixin, ListView):
    """Displays a filterable table of projects.

    Initial display organizes listings by creation date."""

    pass
    # model = Project
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['x'] = 'x'
    #     return context



class ProjectCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """A logged in user with the appropriate permissions can create a project .

    Projects are a large-scale organizational component made up of multiple stories.
    Projects can have stories, assets, notes, discussions,
    simple assets, calendar objects and meta information.
    """
    pass

    model = Project


class ProjectUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """

    """
    pass


class ProjectTeamUpdateView(FormMessagesMixin, UpdateView):
    """

    """
    pass


class ProjectDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class ProjectDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """

    """
    pass
    # model = Project
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['x'] = 'x'
    #     return context


class ProjectAssetTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class ProjectStoryListTemplateView(LoginRequiredMixin, TemplateView):
    """

    """
    pass

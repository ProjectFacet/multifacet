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
ProjectStoryView: Presents list of stories associated with a Project
ProjectTaskView: Presents all tasks associated with a Project
ProjectNoteView: Presents all notes associated with a Project
ProjectScheduleView: Presents all calendar items associated with a Project

"""

from django.shortcuts import render
from django.shortcuts import redirect
from braces.views import LoginRequiredMixin, FormMessagesMixin
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView, DeleteView, FormView, View

from editorial.forms import (
    ProjectForm,
    ProjectTeamForm,
    SimpleImageForm,
    SimpleDocumentForm,
    SimpleImageLibraryAssociateForm,
    SimpleDocumentLibraryAssociateForm,
)

from task.forms import (TaskForm)
from timeline.forms import (EventForm)
from communication.forms import (CommentForm)
from note.forms import (NoteForm)
from editorial.forms import (SimpleImageForm, SimpleDocumentForm)

from editorial.models import (
    Project,
    Story,
)

from communication.models import (
    Discussion,
    Comment,
)


class ProjectCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """A logged in user with the appropriate permissions can create a project.

    Currently limited to StaffJournalist:
    If staff journalists is affiliated, entity_owner = staffjournalist.newsorganization
    If staff journalist is unaffiliated, entity_owner = Null

    Projects are a large-scale organizational component made up of multiple stories.
    Projects can have stories, assets, notes, discussions,
    simple assets, calendar objects and meta information.
    """

    model = Project
    template_name = 'project/project_form.html'
    form_class = ProjectForm

    form_invalid_message = "Something went wrong."
    form_valid_message = "Project created."

    def form_valid(self, form):
        """Save -- but first adding participant_owner and entity_owner if applicable."""

        self.object = form.save(commit=False)
        participant = self.request.user
        self.object.participant_owner = participant
        if participant.staffjournalist:
            entity = participant.staffjournalist.newsorganization
            eo = entity.entity_owner_profile
            self.object.entity_owner = eo
        self.object.save()
        return redirect(self.object)


class ProjectDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """
    Displays project meta, stories, tasks, events, notes, assets.
    """

    model = Project
    template_name = 'project/project_detail.html'

    def get_form_kwargs(self):
        """Pass entity_owner, participant_owner to form."""

        kw = super(ProjectDetailView, self).get_form_kwargs()
        if self.object.entity_owner:
            kw.update({'entity_owner': self.object.entity_owner})
        if self.object.participant_owner == self.request.user:
            kw.update({'participant_owner': self.request.user})
        return kw

    def stories(self):
        """Get all stories associated with project."""

        return self.object.story_set.all()

    def assets(self):
        """Retrieve all assets associated with a project through story items."""

        images = self.object.get_project_images()
        documents = self.object.get_project_documents()
        audio = self.object.get_project_audio()
        video = self.object.get_project_video()

        return {'images': images, 'documents': documents, 'audio': audio, 'video': video}

    def project_discussion(self):
        """Get discussion, comments and comment form for the project."""

        discussion = self.object.discussion
        comments = discussion.comment_set.all().order_by('date')
        form = CommentForm()

        return {'discussion': discussion, 'comments': comments, 'form': form}

    def project_notes(self):
        """Get notes and note form for the project."""

        notes = self.object.notes.all().order_by('-creation_date')
        form = NoteForm()

        return {'notes': notes, 'form': form}

    def project_tasks(self):
        """Get tasks and task form for the project."""

        tasks = self.object.task_set.all()
        identified = self.object.task_set.filter(status="Identified")
        inprogress = self.object.task_set.filter(status="In Progress")
        complete = self.object.task_set.filter(status="Complete")
        identified_ct = identified.count()
        inprogress_ct = inprogress.count()
        complete_ct = complete.count()
        form = TaskForm(organization=self.request.user.organization)

        return {
            'tasks': tasks,
            'identified': identified,
            'inprogress': inprogress,
            'complete': complete,
            'identified_ct': identified_ct,
            'inprogress_ct': inprogress_ct,
            'complete_ct': complete_ct,
            'form': form,
        }

    def events(self):
        """Get events and event form for the project."""

        events = self.object.event_set.all().order_by('-event_date')
        form = EventForm(organization=self.request.user.organization)

        return {'events': events, 'form': form}

    def simple_images(self):
        """Return simple images."""

        images = self.object.simple_image_assets.all()
        form = SimpleImageForm()
        addform = SimpleImageLibraryAssociateForm(organization=self.request.user.organization)
        return {'images': images, 'form': form, 'addform': addform,}

    def simple_documents(self):
        """Return simple documents."""

        documents = self.object.simple_document_assets.all()
        form = SimpleDocumentForm()
        addform = SimpleDocumentLibraryAssociateForm(organization=self.request.user.organization)
        return {'documents': documents, 'form': form, 'addform': addform,}


class ProjectUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """
    Update a project.
    """

    model = Project
    template_name = 'project/project_form.html'
    form_class = ProjectForm

    form_invalid_message = "Something went wrong."
    form_valid_message = "Project updated."

    def get_form_kwargs(self):
        """Pass entity, participant to form."""

        kw = super(ProjectUpdateView, self).get_form_kwargs()
        if self.object.entity_owner:
            kw.update({'entity_owner': self.object.entity_owner})
        if self.object.participant_owner == self.request.user:
            kw.update({'participant_owner': self.request.user})
        return kw

    def get_success_url(self):
        """Return project."""

        return super(ProjectUpdateView, self).get_success_url()


class ProjectDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass





class ProjectTeamUpdateView(FormMessagesMixin, UpdateView):
    """

    """
    pass



class ProjectStoryView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class ProjectAssetView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class ProjectTaskView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class ProjectNoteView(LoginRequiredMixin, TemplateView):
    """

    """
    pass


class ProjectScheduleView(LoginRequiredMixin, FormMessagesMixin, TemplateView):
    """

    """
    pass

# ----------------------------------

class StaffJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return projects of a staff journalist."""
    pass


class UnaffiliatedStaffJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return projects of an unaffiliated staff journalist."""
    pass


class FreelanceJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return projects of a freelance journalist."""
    pass


class NewsOrganizationProjectListView(LoginRequiredMixin, ListView):
    """Return projects for a news organization."""
    pass


class NewsOrganizationNetworkProjectListView(LoginRequiredMixin, ListView):
    """Return projects for a news organization network."""
    pass


# class ProjectListView(LoginRequiredMixin, ListView):
#     """Displays a filterable table of projects.
#
#     Initial display organizes listings by creation date."""
#
#     model = Project
#     template_name = 'project/project_list.html'
#
#     def get_context_data(self, pk, type):
#         if type=='newsorganization':
#             newsorganization = get_object_or_404(NewsOrganization, pk=pk)
#             projects = NewsOrganization.get_projects(newsorganization)
#
#         if type=='newsorganizationnetwork':
#             newsorganizationnetwork = get_object_or_404(NewsOrganizationNetwork, pk=pk)
#             projects = NewsOrganizationNetwork.get_projects(newsorganizationnetwork)
#
#         if type=='staffjournalist':
#             staffjournalist = get_object_or_404(StaffJournalist, pk=pk)
#             projects = StaffJournalist.get_projects(staffjournalist)
#
#         if type=='unaffiliatedstaffjournalist':
#             unaffiliatedstaffjournalist = get_object_or_404(UnaffiliatedStaffJournalist, pk=pk)
#             projects = UnaffiliatedStaffJournalist.get_projects(unaffiliatedstaffjournalist)
#
#         if type=='freelancejournalist':
#             freelancejournalist = get_object_or_404(FreelanceJournalist, pk=pk)
#             projects = FreelanceJournalist.get_projects(freelancejournalist)




    def get_queryset(self):
        """Retrieve appropriate project list."""

        #TODO replace this temporary queryset
        projects = Project.objects.all()

        return projects


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['x'] = 'x'
    #     return context

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
    InternalImageForm,
    InternalDocumentForm,
    InternalImageLibraryAssociateForm,
    InternalDocumentLibraryAssociateForm,
)

from task.forms import (TaskForm)
from timeline.forms import (EventForm)
from communication.forms import (CommentForm)
from note.forms import (NoteForm)

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
    internal assets, calendar objects and meta information.
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

    def internal_images(self):
        """Return internal images."""

        images = self.object.internal_image_assets.all()
        form = InternalImageForm()
        addform = InternalImageLibraryAssociateForm(organization=self.request.user.organization)
        return {'images': images, 'form': form, 'addform': addform,}

    def internal_documents(self):
        """Return internal documents."""

        documents = self.object.internal_document_assets.all()
        form = InternalDocumentForm()
        addform = InternalDocumentLibraryAssociateForm(organization=self.request.user.organization)
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
    """Delete a project and its associated notes, tasks and events.

    Stories and story child objects should not be deleted.

    In this project, we expect deletion to be done via a JS pop-up UI; we don't expect to
    actually use the "do you want to delete this?" Django-generated page. However, this is
    available if useful.
    """

    model = Project
    template_name = "project/project_delete.html'"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post-deletion, return to the project list."""

        return reverse('project_list')


class ProjectTeamUpdateView(FormMessagesMixin, UpdateView):
    """
    Return appropriate participants for selection as team.
    """
    model = Project
    template_name = 'project/projectteam_form.html'
    form_class = ProjectTeamForm
    form_valid_message = "Project team updated."
    form_invalid_message = "Something went wrong. Please check the form."

    def get_form_kwargs(self):
        kw = super(ProjectTeamUpdateView, self).get_form_kwargs()
        if self.object.entity_owner:
            kw.update({'entity_owner': self.object.entity_owner})
        if self.object.participant_owner == self.request.user:
            kw.update({'participant_owner': self.request.user})
        return kw

    def project_details(self):
        """Get project object to display information."""

        project = Project.objects.get(id=self.kwargs['pk'])
        return project

    def form_valid(self, form):
        """Handle submission of form."""

        project = Project.objects.get(id=self.kwargs['pk'])
        team_list = form.cleaned_data['team']
        project.team = team_list
        project.save()

        return redirect('project_detail', pk=project.id)


class ProjectStoryView(LoginRequiredMixin, TemplateView):
    """Return and display all the stories associated with a project."""

    template_name = 'project/project_stories.html'

    def get_context_data(self, pk):
        """Return all the stories."""

        project = get_object_or_404(Project, id=pk)
        stories = project.get_project_stories()

        # For each story, use the first image (if any) as the "featured image"

        for story in stories:
            images = story.get_story_images()
            if images:
                story.featured_image = images[0]

        return {'project': project, 'stories': stories}


class ProjectAssetView(LoginRequiredMixin, TemplateView):
    """Display media associated with a project."""

    template_name = 'project/project_assets.html'

    def get_context_data(self, pk):
        """Return all the (complex) assets associated with a project."""

        project = get_object_or_404(Project, id=pk)
        images = project.get_project_images()
        documents = project.get_project_documents()
        audio = project.get_project_audio()
        video = project.get_project_video()

        return {
            'project': project,
            'images': images,
            'documents': documents,
            'audio': audio,
            'video': video,
        }


class ProjectTaskView(LoginRequiredMixin, TemplateView):
    """Display and manage project tasks."""

    context_object_name = 'tasks'
    template_name = 'project/project_tasks.html'
    form_class = TaskForm

    form_invalid_message = "Something went wrong. Check the form."
    form_valid_message = "Task created."

    def get_form_kwargs(self):
        """Pass organization to form."""

        kw = super(ProjectTaskView, self).get_form_kwargs()
        if self.object.entity_owner:
            kw.update({'entity_owner': self.object.entity_owner})
        if self.object.participant_owner == self.request.user:
            kw.update({'participant_owner': self.request.user})
        return kw

    def get_context_data(self, **kwargs):
        """Return tasks belonging to the story."""

        context = super(ProjectTaskView, self).get_context_data(**kwargs)
        project = get_object_or_404(Project, id=self.kwargs['pk'])
        tasks = project.task_set.all()
        count = tasks.count()
        identified_ct = project.task_set.filter(status="Identified").count()
        inprogress_ct = project.task_set.filter(status="In Progress").count()
        complete_ct = project.task_set.filter(status="Complete").count()
        # ratio of complete to total number of tasks
        if complete_ct>0:
            progress = 100 * float(complete_ct)/float(count)
        else:
            progress = 0
        context['project'] = project
        context['tasks'] = tasks
        context['progress'] = progress
        context['identified_ct'] = identified_ct
        context['inprogress_ct'] = inprogress_ct
        context['complete_ct'] = complete_ct
        return context


class ProjectNoteView(LoginRequiredMixin, TemplateView):
    """Display all of the notes for a project."""

    template_name = 'project/project_notes.html'

    def get_context_data(self, pk):
        project = get_object_or_404(Project, pk=pk)
        form = NoteForm()
        notes = project.notes.all().order_by('-creation_date')
        return {
            'project': project,
            'form': form,
            'notes': notes,
        }


class ProjectScheduleView(LoginRequiredMixin, FormMessagesMixin, TemplateView):
    """Return JSON of project schedule information."""

    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['pk']
        project = Project.objects.get(id=project_id)
        project_calendar = project.get_project_schedule()

        return HttpResponse(json.dumps(project_calendar), content_type='application/json')

# ----------------------------------

class StaffJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return projects a staff journalist should have access to.

    Note: the personalized list of projects a participant is associated
    with is available in their dashboard  or detail view.
    """

    model = Project
    template_name = 'project/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participant = self.request.user
        context['projects'] = participant.staffjournalist.newsorganization.get_projects()
        return context


class UnaffiliatedStaffJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return projects of an unaffiliated staff journalist.

    Since an UnaffiliatedStaffJournalist does not have an organization,
    returns list of projects owned by USJ or USJ is a project_team_member, partner.

    Note: the personalized list of projects a participant is associated
    with is available in their dashboard  or detail view.
    """

    model = Project
    template_name = 'project/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participant = self.request.user
        context['projects'] = participant.unaffiliatedstaffjournalist.get_projects()
        return context


class FreelanceJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return projects of a freelance journalist.

    Since a FreelanceJournalist does not have an organization,
    returns list of projects owned by FJ or FJ is a project_team_member, partner.

    Note: the personalized list of projects a participant is associated
    with is available in their dashboard  or detail view.
    """

    model = Project
    template_name = 'project/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participant = self.request.user
        context['projects'] = participant.freelancejournalist.get_projects()
        return context


class NewsOrganizationProjectListView(LoginRequiredMixin, ListView):
    """Return projects for a news organization."""

    model = Project
    template_name = 'project/project_list.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        newsorganization = NewsOrganization.objects.get(pk=pk)
        context['projects'] = newsorganization.get_projects()
        return context


class NewsOrganizationNetworkProjectListView(LoginRequiredMixin, ListView):
    """Return projects for a news organization network."""

    model = Project
    template_name = 'project/project_list.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        newsorganizationnetwork = NewsOrganizationNetwork.objects.get(pk=pk)
        context['projects'] = newsorganizationnetwork.get_projects()
        return context


class ProjectListRedirectView(LoginRequiredMixin, ListView):
    """Facilitates generic linking of projects by at /project/list by
    redirecting user to appropriate list for their user profile.
    """

    def get(self, request, *args, **kwargs):

        participant = self.request.user

        if participant.staffjournalist:
            return redirect('editorial:staff_project_list')
        elif participant.unaffiliatedstaffjournalist:
            return redirect('editorial:unaffiliated_project_list')
        elif participant.freelancejournalist:
            return redirect('editorial:freelance_project_list')
        else:
            return redirect('dashboard_account_requested')

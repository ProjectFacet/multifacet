"""Story Views for Facet/Editorial.

A story is the container for a story.

A story can have either one Item which is the single version of the story
or it can contain multiple Items to hold different versions of the story.
For example, one Item could be the text of an article. But there can be
additional Items that are that article in a different language or a different
version, such as a host wrap for radio. The idea is to contain the different
versions of a story together.

StoryListView: List of stories appropriate for context.
    - A StaffJournalist would see:
        /<newsorg slug>/stories: all stories owned by their NewsOrganization
        /<newsorg network slug>/stories: all stories owned or partnered with NewsOrganizationNetwork
    - A FreelanceJournalist would see:
        /dashboard/stories: all stories they own or are assigned to

StoryCreateView: View that handles creating a new Story
StoryUpdateView: View that handles updating a Story's attributes
StoryTeamUpdateView: View to edit a Story's team
StoryDeleteView: View to delete a story. A story can be deleted by Participant who created it
    or by an admin of the entity the story is associated with.
StoryDetailView: View that presents all of the details and associations for a Story
StoryAssetView: Presents asset library of a Story
StoryItemView: Presents list of Items associated with a Story
StoryTaskView: Presents all tasks associated with a Story
StoryNoteView: Presents all notes associated with a Story
StoryScheduleView: Presents all calendar items associated with a Story


"""

from django.shortcuts import render
from django.shortcuts import redirect
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
            eo = entity.entity_owner_profile
            self.object.entity_owner = eo
        self.object.save()
        return redirect(self.object)


class StoryDetailView(LoginRequiredMixin, FormMessagesMixin, DetailView):
    """
    Displays project meta, stories, tasks, events, notes, assets.
    """

    model = Story
    template_name = 'story/story_detail.html'

    def get_form_kwargs(self):
        """Pass entity_owner, participant_owner to form."""

        kw = super(StoryDetailView, self).get_form_kwargs()
        if self.object.entity_owner:
            kw.update({'entity_owner': self.object.entity_owner})
        if self.object.participant_owner == self.request.user:
            kw.update({'participant_owner': self.request.user})
        return kw

    def items(self):
        """Get all items associated with project."""

        return self.object.item_set.all()

    def assets(self):
        """Retrieve all assets associated with a story through items."""

        images = self.object.get_story_images()
        documents = self.object.get_story_documents()
        audio = self.object.get_story_audio()
        video = self.object.get_story_video()

        return {'images': images, 'documents': documents, 'audio': audio, 'video': video}

    def story_discussion(self):
        """Get discussion, comments and comment form for the story."""

        discussion = self.object.discussion
        comments = discussion.comment_set.all().order_by('date')
        form = CommentForm()

        return {'discussion': discussion, 'comments': comments, 'form': form}

    def story_notes(self):
        """Get notes and note form for the story."""

        notes = self.object.notes.all().order_by('-creation_date')
        form = NoteForm()

        return {'notes': notes, 'form': form}

    def story_tasks(self):
        """Get tasks and task form for the story."""

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
        """Get events and event form for the story."""

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


class StoryUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """
    Update a story.
    """

    model = Story
    template_name = 'story/story_form.html'
    form_class = StoryForm

    form_invalid_message = "Something went wrong."
    form_valid_message = "Story updated."

    def get_form_kwargs(self):
        """Pass entity, participant to form."""

        kw = super(StoryUpdateView, self).get_form_kwargs()
        if self.object.entity_owner:
            kw.update({'entity_owner': self.object.entity_owner})
        if self.object.participant_owner == self.request.user:
            kw.update({'participant_owner': self.request.user})
        return kw

    def get_success_url(self):
        """Return story."""

        return super(StoryUpdateView, self).get_success_url()

class StoryDeleteView(LoginRequiredMixin, FormMessagesMixin, DeleteView):
    """

    """
    pass


class StoryTeamUpdateView(FormMessagesMixin, UpdateView):
    """

    """
    pass




class StoryItemView(LoginRequiredMixin, TemplateView):
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


# -------------------------
# ----------------------------------

class StaffJournalistStoryListView(LoginRequiredMixin, ListView):
    """Return stories of a staff journalist."""
    pass


class UnaffiliatedStaffJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return stories of an unaffiliated staff journalist."""
    pass


class FreelanceJournalistProjectListView(LoginRequiredMixin, ListView):
    """Return stories of a freelance journalist."""
    pass


class NewsOrganizationProjectListView(LoginRequiredMixin, ListView):
    """Return stories for a news organization."""
    pass


class NewsOrganizationNetworkProjectListView(LoginRequiredMixin, ListView):
    """Return stories for a news organization network."""
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

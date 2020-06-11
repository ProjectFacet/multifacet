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

class StoryCreateView(LoginRequiredMixin, FormMessagesMixin, CreateView):
    """A logged in user with the appropriate permissions can create a story.

    Stories can have items, assets, notes, discussions,
    internal assets, calendar objects and meta information.
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
    Displays story meta, stories, tasks, events, notes, assets.
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
        """Get all items associated with story."""

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
    """Delete a story and its associated notes, tasks and events.

    Items should be deleted.

    In this story, we expect deletion to be done via a JS pop-up UI; we don't expect to
    actually use the "do you want to delete this?" Django-generated page. However, this is
    available if useful.
    """

    model = Story
    template_name = "story/story_delete.html'"

    form_valid_message = "Deleted."
    form_invalid_message = "Please check form."

    def get_success_url(self):
        """Post-deletion, return to the story list."""

        return reverse('story_list')


class StoryTeamUpdateView(FormMessagesMixin, UpdateView):
    """
    Return appropriate participants for selection as team.
    """

    model = Story
    template_name = 'story/storyteam_form.html'
    form_class = StoryTeamForm
    form_valid_message = "Story team updated."
    form_invalid_message = "Something went wrong. Please check the form."

    def get_form_kwargs(self):
        kw = super(StoryTeamUpdateView, self).get_form_kwargs()
        if self.object.entity_owner:
            kw.update({'entity_owner': self.object.entity_owner})
        if self.object.participant_owner == self.request.user:
            kw.update({'participant_owner': self.request.user})
        return kw

    def story_details(self):
        """Get story object to display information."""

        story = Story.objects.get(id=self.kwargs['pk'])
        return story

    def form_valid(self, form):
        """Handle submission of form."""

        story = Story.objects.get(id=self.kwargs['pk'])
        team_list = form.cleaned_data['team']
        story.team = team_list
        story.save()

        return redirect('story_detail', pk=story.id)


class StoryItemView(LoginRequiredMixin, TemplateView):
    """Return and display all the items associated with a story."""

    template_name = 'story/story_items.html'

    def get_context_data(self, pk):
        """Return all the items."""

        story = get_object_or_404(Story, id=pk)
        items = story.item_set.all()

        # For each item, use the first image (if any) as the "featured image"

        for item in items:
            images = item.image_set.all()
            if images:
                item.featured_image = images[0]

        return {'story': story, 'items':items}


class StoryAssetView(LoginRequiredMixin, TemplateView):
    """Display media associated with a story."""

    template_name = 'story/story_assets.html'

    def get_context_data(self, pk):
        """Return all the (complex) assets associated with a story."""

        story = get_object_or_404(Story, id=pk)
        images = story.get_story_images()
        documents = story.get_story_documents()
        audio = story.get_story_audio()
        video = story.get_story_video()

        return {
            'story': story,
            'images': images,
            'documents': documents,
            'audio': audio,
            'video': video,
        }


class StoryTaskView(LoginRequiredMixin, TemplateView):
    """Create a story task."""

    context_object_name = 'tasks'
    template_name = 'story/story_tasks.html'
    form_class = TaskForm

    form_invalid_message = "Something went wrong. Check the form."
    form_valid_message = "Task created."

    def get_form_kwargs(self):
        """Pass organization to form."""

        kw = super(StoryTaskView, self).get_form_kwargs()
        kw.update({'organization': self.request.user.organization})
        return kw

    def get_context_data(self, **kwargs):
        """Return tasks belonging to the story."""

        context = super(StoryTaskView, self).get_context_data(**kwargs)
        story = get_object_or_404(Story, id=self.kwargs['pk'])
        tasks = story.task_set.all()
        count = tasks.count()
        identified_ct = story.task_set.filter(status="Identified").count()
        inprogress_ct = story.task_set.filter(status="In Progress").count()
        complete_ct = story.task_set.filter(status="Complete").count()
        # ratio of complete to total number of tasks
        if complete_ct>0:
            progress = 100 * float(complete_ct)/float(count)
        else:
            progress = 0
        context['story'] = story
        context['tasks'] = tasks
        context['progress'] = progress
        context['identified_ct'] = identified_ct
        context['inprogress_ct'] = inprogress_ct
        context['complete_ct'] = complete_ct
        return context


class StoryNoteView(LoginRequiredMixin, TemplateView):
    """Display all of the notes for a story."""

    template_name = 'story/story_notes.html'

    def get_context_data(self, pk):
        story = get_object_or_404(Story, pk=pk)
        form = NoteForm()
        notes = story.notes.all().order_by('-creation_date')
        return {
            'story': story,
            'form': form,
            'notes': notes,
        }


class StoryScheduleView(LoginRequiredMixin, FormMessagesMixin, TemplateView):
    """Return JSON of story schedule information."""

    def get(self, request, *args, **kwargs):
        story_id = self.kwargs['pk']
        story = Story.objects.get(id=story_id)
        story_calendar = story.get_story_schedule()

        return HttpResponse(json.dumps(story_calendar), content_type='application/json')


# ----------------------------------

class StaffJournalistStoryListView(LoginRequiredMixin, ListView):
    """Return stories a staff journalist should have access to.

    Note: the personalized list of stories a participant is associated
    with is available in their dashboard  or detail view.
    """

    model = Project
    template_name = 'story/story_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participant = self.request.user
        context['stories'] = participant.staffjournalist.newsorganization.get_stories()
        return context


class UnaffiliatedStaffJournalistStoryListView(LoginRequiredMixin, ListView):
    """Return stories of an unaffiliated staff journalist.

    Since an UnaffiliatedStaffJournalist does not have an organization,
    returns list of stories owned by USJ or USJ is a story_team_member, partner.

    Note: the personalized list of stories a participant is associated
    with is available in their dashboard  or detail view.
    """

    model = Project
    template_name = 'story/story_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participant = self.request.user
        context['stories'] = participant.unaffiliatedstaffjournalist.get_stories()
        return context


class FreelanceJournalistStoryListView(LoginRequiredMixin, ListView):
    """Return stories of a freelance journalist.

    Since a FreelanceJournalist does not have an organization,
    returns list of stories owned by FJ or FJ is a story_team_member, partner.

    Note: the personalized list of stories a participant is associated
    with is available in their dashboard  or detail view.
    """

    model = Project
    template_name = 'story/story_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participant = self.request.user
        context['stories'] = participant.freelancejournalist.get_stories()
        return context


class NewsOrganizationStoryListView(LoginRequiredMixin, ListView):
    """Return stories for a news organization."""

    model = Project
    template_name = 'story/story_list.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        newsorganization = NewsOrganization.objects.get(pk=pk)
        context['stories'] = newsorganization.get_stories()
        return context


class NewsOrganizationNetworkStoryListView(LoginRequiredMixin, ListView):
    """Return stories for a news organization network."""
    """Return stories for a news organization network."""

    model = Project
    template_name = 'story/story_list.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        newsorganizationnetwork = NewsOrganizationNetwork.objects.get(pk=pk)
        context['stories'] = newsorganizationnetwork.get_stories()
        return context




class StoryListRedirectView(LoginRequiredMixin, ListView):
    """Facilitates generic linking of stories by at /story/list by
    redirecting user to appropriate list for their user profile.
    """

    def get(self, request, *args, **kwargs):

        participant = self.request.user

        if participant.staffjournalist:
            return redirect('editorial:staff_story_list')
        elif participant.unaffiliatedstaffjournalist:
            return redirect('editorial:unaffiliated_story_list')
        elif participant.freelancejournalist:
            return redirect('editorial:freelance_story_list')
        else:
            return redirect('dashboard_account_requested')

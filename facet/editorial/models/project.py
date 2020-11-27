from django.urls import reverse
from django.db import models
# from django.db.models import Q
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from base.models import Participant, Anchor, EntityOwner, Partner
from note.models import Note


class Project(models.Model):
    """A project.

    Projects are a large-scale organizational component made up of multiple stories.
    The primary use is as an organization mechanism for complex
    collaborative projects. Projects can have stories, assets, notes, discussions,
    governing documents, events, calendars and meta information.
    """

    # relationships
    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)

    participant_owner = models.OneToOneField(
        Participant,
        help_text = 'Participant who created/owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    team = models.ManyToManyField(
        Participant,
        related_name='project_team_members',
        help_text='Contributing participant.',
        blank=True,
    )

    partner_with = models.ManyToManyField(
        Partner,
        related_name='roject_collaboration_partners',
        help_text='Partner profiles selected to have collaborative access.',
        blank=True,
    )

    # details
    name = models.CharField(
        max_length=75,
        help_text='The name identifying the project.'
    )

    desc = models.TextField(
        blank=True,
        help_text='Short description of a story.'
    )


    creation_date = models.DateTimeField(
        auto_now_add=True,
    )

    sensitive = models.BooleanField(
        default=False,
        help_text='Is a project sensitive, for limited viewing?'
    )

    collaborate = models.BooleanField(
        default=False,
        help_text='The project is being collaborated on with partners.'
    )

    archived = models.BooleanField(
        default=False,
        help_text='Is the content no longer active and needed?'
    )

    website = models.URLField(
        max_length=250,
        blank=True,
        help_text = 'Project website if applicable.'
    )

    # notes
    notes = models.ManyToManyField(Note, blank=True)

    # internal assets
    internal_image_assets = models.ManyToManyField('internalasset.InternalImage', blank=True)
    internal_document_assets = models.ManyToManyField('internalasset.InternalDocument', blank=True)
    internal_audio_assets = models.ManyToManyField('internalasset.InternalAudio', blank=True)
    internal_video_assets = models.ManyToManyField('internalasset.InternalVideo', blank=True)

    project_logo = models.ImageField(
        upload_to='projects',
        blank=True,
    )

    display_logo = ImageSpecField(
        source='project_logo',
        processors=[SmartResize(500, 500)],
        format='JPEG',
    )


    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = "Projects"
        ordering = ['-creation_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('editorial:project_detail', kwargs={'pk': self.id})

    @property
    def description(self):
        return "{description}".format(description=self.project_description)

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Project"

    #---------------------------------------------------------------------------
    # Methods
    #---------------------------------------------------------------------------

    def get_team_vocab(self):
        """
        Team vocab should include:
        if partner_with:
            partipants from partner_profiles of actors or entities listed
        if entity_owner:
            staff_team of entity_owner
        if assignment.project = self:
            freelancer
        if project.guest:
            guest participant
        if participant_owner:
            participant_owner
        """

        from entity.models import NewsOrganization, NewsOrganizationNetwork
        from freelance.models import Assignment

        partner_profiles = []
        team_vocab = []
        if self.partner_with:
            # retrieve partner profiles of participants and entities
            partners = self.partner_with.all()
            for entry in partners:
                if entry.partner_type=='PARTICIPANT' or entry.partner_type=='NEWS ORGANIZATION':
                    partner_profiles.extend(entry)
                if entry.partner_type=='NEWS ORGANIZATION NETWORK':
                    m_to_p = NewsOrganizationNetwork.convert_members_to_partners(entry)
                    partner_profiles.extend(m_to_p)
        else:
            # retrieve partner vocabulary based on owner
            if self.entity_owner and entity_owner.type=='NewsOrganization':
                newsorganization = NewsOrganization.objects.get(id=entity_owner.owner_id)
                associations_and_networks = NewsOrganization.get_partner_vocab(newsorganization)
                for entry in associations_and_networks:
                    if entry.type=='PARTICIPANT':
                        partner_profiles.extend(entry)
                    else:
                        m_to_p = NewsOrganizationNetwork.convert_members_to_partners(entry)
                        partner_profiles.extend(m_to_p)
            # if no entity_owner, participant_owner is team
            elif self.participant_owner and not entity_owner:
                team_vocab.extend(self.participant_owner)

        # convert profiles to participants
        for entry in partner_profiles:
            if entry.partner_type=='PARTICIPANT':
                team_vocab.extend(entry.participant)
            else:
                team = NewsOrganization.get_staff_team(entry.newsorganization)
                team_vocab.extend(team_vocab)

        # Check for freelance assignment
        assignment = Assignment.objects.filter(project=self)
        if assignment:
            team_vocab.extend(assignment.freelancer.participant)
        # Check for guests
        # TODO
        return team_vocab


    def get_project_images(self):
        """Return all image assets associated with items that are part of a project."""

        # get all original stories associated with a project
        project_stories = self.story_set.filter(original_story=True).all()
        # get all image assets associated with those stories.
        project_images = []
        for story in project_stories:
            images=Story.get_story_images(story)
            project_images.extend(images)
        return set(project_images)

    def get_project_documents(self):
        """Return all document assets associated with items that are part of a project."""

        # get all original stories associated with a project
        project_stories = self.story_set.filter(original_story=True).all()
        # get all document assets associated with those stories.
        project_documents = []
        for story in project_stories:
            documents=story.get_story_documents()
            project_documents.extend(documents)
        return set(project_documents)

    def get_project_audio(self):
        """Return all audio assets associated with items that are part of a project."""

        # get all original stories associated with a project
        project_stories = self.story_set.filter(original_story=True).all()
        # get all audio assets associated with those stories.
        project_audio = []
        for story in project_stories:
            audio=story.get_story_audio()
            project_audio.extend(audio)
        return set(project_audio)

    def get_project_video(self):
        """Return all video assets associated with items that are part of a project."""

        # get all original stories associated with a project
        project_stories = self.story_set.filter(original_story=True).all()
        # get all video assets associated with those stories.
        project_video = []
        for story in project_stories:
            videos=story.get_story_video()
            project_video.extend(videos)
        return set(project_video)

    # TODO Delete
    # def get_project_tasks(self):
    #     """Return all tasks associated with a project."""
    #     return self.task_set.all()

    # def get_project_stories(self):
    #     """Return all original stories associated with a project."""
    #     return self.story_set.filter(original_story=True).all()

    # def get_project_event_schedule(self):
    #     """Return project events for a project.
    #
    #     Used for returning a single project's event schedule.
    #     """
    #
    #     data = []
    #
    #     project = Project.objects.get(pk=self.id)
    #
    #     # gather schedule dates for all project events
    #     if project.event_set.all():
    #         for event in project.event_set.filter(event_type="Hosting"):
    #             hosting_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             hosting_event_dict['id'] = event.id
    #             hosting_event_dict['title'] = event.name
    #             hosting_event_dict['event_date'] = item_date.isoformat()
    #             hosting_event_dict['url'] = event.get_absolute_url()
    #             hosting_event_dict['start'] = item_date.isoformat()
    #             hosting_event_dict['end'] = item_date.isoformat()
    #             hosting_event_dict['overlap'] = True
    #             hosting_event_dict['all_day'] = False
    #             hosting_event_dict['backgroundColor'] = '#3F51B5'
    #             hosting_event_dict['textColor'] = 'fff'
    #             hosting_event_dict['class'] = "calevent"
    #
    #             data.append(hosting_event_dict)
    #
    #         for event in project.event_set.filter(event_type="Reporting"):
    #             reporting_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             reporting_event_dict['id'] = event.id
    #             reporting_event_dict['title'] = event.name
    #             reporting_event_dict['event_date'] = item_date.isoformat()
    #             reporting_event_dict['url'] = event.get_absolute_url()
    #             reporting_event_dict['start'] = item_date.isoformat()
    #             reporting_event_dict['end'] = item_date.isoformat()
    #             reporting_event_dict['overlap'] = True
    #             reporting_event_dict['all_day'] = False
    #             reporting_event_dict['backgroundColor'] = '#2196F3'
    #             reporting_event_dict['textColor'] = 'fff'
    #             reporting_event_dict['class'] = "calevent"
    #
    #             data.append(reporting_event_dict)
    #
    #         for event in project.event_set.filter(event_type="Administrative"):
    #             administrative_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             administrative_event_dict['id'] = event.id
    #             administrative_event_dict['title'] = event.name
    #             administrative_event_dict['event_date'] = item_date.isoformat()
    #             administrative_event_dict['url'] = event.get_absolute_url()
    #             administrative_event_dict['start'] = item_date.isoformat()
    #             administrative_event_dict['end'] = item_date.isoformat()
    #             administrative_event_dict['overlap'] = True
    #             administrative_event_dict['all_day'] = False
    #             administrative_event_dict['backgroundColor'] = '#03A9F4'
    #             administrative_event_dict['textColor'] = 'fff'
    #             administrative_event_dict['class'] = "calevent"
    #
    #             data.append(administrative_event_dict)
    #
    #         for event in project.event_set.filter(event_type="Other"):
    #             other_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             other_event_dict['id'] = event.id
    #             other_event_dict['title'] = event.name
    #             other_event_dict['event_date'] = item_date.isoformat()
    #             other_event_dict['url'] = event.get_absolute_url()
    #             other_event_dict['start'] = item_date.isoformat()
    #             other_event_dict['end'] = item_date.isoformat()
    #             other_event_dict['overlap'] = True
    #             other_event_dict['all_day'] = False
    #             other_event_dict['backgroundColor'] = '#00BCD4'
    #             other_event_dict['textColor'] = 'fff'
    #             other_event_dict['class'] = "calevent"
    #
    #             data.append(other_event_dict)
    #
    #     return data

    # def get_project_schedule(self):
    #     """Return all the relevant dates for a project.
    #     Used for returning a single project's schedule.
    #
    #     Includes:
    #     From story:
    #         story_share_date
    #         item due_edit
    #         item run_date
    #     From project:
    #         event event_date
    #         task due_date
    #     """
    #
    #     data = []
    #
    #     project = Project.objects.get(pk=self.id)
    #
    #     # gather dates for story sharing and story items for a project
    #     if project.story_set:
    #         for story in project.story_set.all():
    #             single_story_dates = story.get_story_items_schedule()
    #             data.extend(single_story_dates)
    #
    #     # gather schedule dates for all story events
    #     if project.event_set.all():
    #         for event in project.event_set.filter(event_type="Hosting"):
    #             hosting_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             hosting_event_dict['id'] = event.id
    #             hosting_event_dict['title'] = event.name
    #             hosting_event_dict['event_date'] = item_date.isoformat()
    #             hosting_event_dict['url'] = event.get_absolute_url()
    #             hosting_event_dict['start'] = item_date.isoformat()
    #             hosting_event_dict['end'] = item_date.isoformat()
    #             hosting_event_dict['overlap'] = True
    #             hosting_event_dict['all_day'] = False
    #             hosting_event_dict['backgroundColor'] = '#3F51B5'
    #             hosting_event_dict['textColor'] = 'fff'
    #             hosting_event_dict['class'] = "calevent"
    #
    #             data.append(hosting_event_dict)
    #
    #         for event in project.event_set.filter(event_type="Reporting"):
    #             reporting_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             reporting_event_dict['id'] = event.id
    #             reporting_event_dict['title'] = event.name
    #             reporting_event_dict['event_date'] = item_date.isoformat()
    #             reporting_event_dict['url'] = event.get_absolute_url()
    #             reporting_event_dict['start'] = item_date.isoformat()
    #             reporting_event_dict['end'] = item_date.isoformat()
    #             reporting_event_dict['overlap'] = True
    #             reporting_event_dict['all_day'] = False
    #             reporting_event_dict['backgroundColor'] = '#2196F3'
    #             reporting_event_dict['textColor'] = 'fff'
    #             reporting_event_dict['class'] = "calevent"
    #
    #             data.append(reporting_event_dict)
    #
    #         for event in project.event_set.filter(event_type="Administrative"):
    #             administrative_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             administrative_event_dict['id'] = event.id
    #             administrative_event_dict['title'] = event.name
    #             administrative_event_dict['event_date'] = item_date.isoformat()
    #             administrative_event_dict['url'] = event.get_absolute_url()
    #             administrative_event_dict['start'] = item_date.isoformat()
    #             administrative_event_dict['end'] = item_date.isoformat()
    #             administrative_event_dict['overlap'] = True
    #             administrative_event_dict['all_day'] = False
    #             administrative_event_dict['backgroundColor'] = '#03A9F4'
    #             administrative_event_dict['textColor'] = 'fff'
    #             administrative_event_dict['class'] = "calevent"
    #
    #             data.append(administrative_event_dict)
    #
    #         for event in project.event_set.filter(event_type="Other"):
    #             other_event_dict = {}
    #
    #             item_date = event.event_date
    #
    #             other_event_dict['id'] = event.id
    #             other_event_dict['title'] = event.name
    #             other_event_dict['event_date'] = item_date.isoformat()
    #             other_event_dict['url'] = event.get_absolute_url()
    #             other_event_dict['start'] = item_date.isoformat()
    #             other_event_dict['end'] = item_date.isoformat()
    #             other_event_dict['overlap'] = True
    #             other_event_dict['all_day'] = False
    #             other_event_dict['backgroundColor'] = '#00BCD4'
    #             other_event_dict['textColor'] = 'fff'
    #             other_event_dict['class'] = "calevent"
    #
    #             data.append(other_event_dict)
    #
    #     # gather schedule dates for all story tasks
    #     if project.task_set.all():
    #         for task in project.task_set.all():
    #             task_event_dict = {}
    #
    #             item_date = task.due_date
    #
    #             task_event_dict['id'] = task.id
    #             task_event_dict['title'] = task.name
    #             task_event_dict['due_date'] = item_date.isoformat()
    #             task_event_dict['url'] = task.get_absolute_url()
    #             task_event_dict['start'] = item_date.isoformat()
    #             task_event_dict['end'] = item_date.isoformat()
    #             task_event_dict['overlap'] = True
    #             task_event_dict['all_day'] = False
    #             task_event_dict['backgroundColor'] = '#7E57C2'
    #             task_event_dict['textColor'] = 'fff'
    #             task_event_dict['class'] = "calevent"
    #
    #             data.append(task_event_dict)
    #
    #     return data

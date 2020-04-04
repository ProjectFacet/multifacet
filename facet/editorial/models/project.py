# # from django.core.urlresolvers import reverse
# from django.db import models
# # from django.db.models import Q
# # from imagekit.models import ImageSpecField
# # from pilkit.processors import SmartResize
#
# from base.models import Participant
# from entity.NewsOrganization import NewsOrganization
# from discussion.models import Discussion, Comment
# from task.models import Task
# from event.models import Event
# from note.models import Note
# from .asset_image import ImageAsset, SimpleImage
# from .asset_document import DocumentAsset, SimpleDocument
# from .asset_audio import AudioAsset, SimpleAudio,
# from .asset_video import VideoAsset, SimpleVideo,
# from .story import Story
# from .item import Item
# from .item_template import ItemTemplate
# from .content_license import ContentLicense
# from .tag import Tag
#
#
# #-----------------------------------------------------------------------#
# #  PROJECT
# #-----------------------------------------------------------------------#
#
# class Project(models.Model):
#     """A project.
#
#     Projects are a large-scale organizational component made up of multiple stories.
#     The primary use is as an organization mechanism for complex
#     collaborative projects. Projects can have stories, assets, notes, discussions,
#     governing documents, events, calendars and meta information.
#     """
#
#     name = models.CharField(
#         max_length=75,
#         help_text='The name identifying the project.'
#     )
#
#     project_description = models.TextField(
#         blank=True,
#         help_text='Short description of a project.',
#     )
#
#     # owner = models.ForeignKey(
#     #     Participant,
#     #     related_name='project_owner',
#     #     help_text='The participant that created the project.'
#     # )
#
#     # Entity Owner
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     # team = models.ManyToManyField(
#     #     Participant,
#     #     related_name='project_team_member',
#     #     help_text='Participant contributing to the project.',
#     #     blank=True,
#     # )
#
#     # creation_date = models.DateTimeField(
#     #     auto_now_add=True,
#     # )
#
#     # sensitive = models.BooleanField(
#     #     default=False,
#     #     help_text='Is a project sensitive, for limited viewing?'
#     # )
#
#     # collaborate = models.BooleanField(
#     #     default=False,
#     #     help_text='The project is being collaborated on with a network.'
#     # )
#
#     # FIXME Create ManyToMany Generic relation to include multiple entities as options
#     # collaborate_with = models.ManyToManyField(
#     #     NewsOrganization,
#     #     related_name='project_collaborated_with_organization',
#     #     help_text='NewsOrganization ids that a project is open to collaboration with.',
#     #     blank=True,
#     # )
#
#     # archived = models.BooleanField(
#     #     default=False,
#     #     help_text='Is the content no longer active and needed?'
#     # )
#
#     # discussions = GenericRelation(Discussion)
#     # notes = GenericRelation(Note)
#     # tasks = GenericRelation(Task)
#     # events = GenericRelation(Event)
#
#     # # project site if different than organization
#     # website = models.URLField(
#     #     max_length=250,
#     #     blank=True,
#     # )
#
#     # # assets
#     # simple_image_assets = models.ManyToManyField(
#     #     SimpleImage,
#     #     blank=True,
#     # )
#
#     # simple_document_assets = models.ManyToManyField(
#     #     SimpleDocument,
#     #     blank=True,
#     # )
#
#     # simple_audio_assets = models.ManyToManyField(
#     #     SimpleAudio,
#     #     blank=True,
#     # )
#
#     # simple_video_assets = models.ManyToManyField(
#     #     SimpleVideo,
#     #     blank=True,
#     # )
#
#     # project_logo = models.ImageField(
#     #     upload_to='projects',
#     #     blank=True,
#     # )
#
#     # display_logo = ImageSpecField(
#     #     source='project_logo',
#     #     processors=[SmartResize(500, 500)],
#     #     format='JPEG',
#     # )
#
#
#     class Meta:
#         verbose_name = 'Project'
#         verbose_name_plural = "Projects"
#         ordering = ['-creation_date']
#
#     def __str__(self):
#         return self.name
#
#     # def get_absolute_url(self):
#     #     return reverse('project_detail', kwargs={'pk': self.id})
#
#     @property
#     def description(self):
#         return "{description}".format(description=self.project_description)
#
#     @property
#     def search_title(self):
#         return self.name
#
#     @property
#     def type(self):
#         return "Project"
#
#     #---------------------------------------------------------------------------
#     # Methods
#     #---------------------------------------------------------------------------
#
#     # FIXME : Participant > Staff Journalist + Freelancer filtering needed
#     # def get_project_team_vocab(self):
#     #     """Return queryset with org participants and participants from collaboration orgs for a project."""
#     #
#     #     collaborators = self.collaborate_with.all()
#     #     project_team = Participant.objects.filter(Q(Q(organization=self.organization) | Q(organization__in=collaborators)))
#     #     return project_team
#
#     # def get_project_images(self):
#     #     """Return all image assets associated with items that are part of a project."""
#     #
#     #     # get all original stories associated with a project
#     #     project_stories = self.story_set.filter(original_story=True).all()
#     #     # get all image assets associated with those stories.
#     #     project_images = []
#     #     for story in project_stories:
#     #         images=Story.get_story_images(story)
#     #         project_images.extend(images)
#     #     return set(project_images)
#
#     # def get_project_documents(self):
#     #     """Return all document assets associated with items that are part of a project."""
#     #
#     #     # get all original stories associated with a project
#     #     project_stories = self.story_set.filter(original_story=True).all()
#     #     # get all document assets associated with those stories.
#     #     project_documents = []
#     #     for story in project_stories:
#     #         documents=story.get_story_documents()
#     #         project_documents.extend(documents)
#     #     return set(project_documents)
#
#     # def get_project_audio(self):
#     #     """Return all audio assets associated with items that are part of a project."""
#     #
#     #     # get all original stories associated with a project
#     #     project_stories = self.story_set.filter(original_story=True).all()
#     #     # get all audio assets associated with those stories.
#     #     project_audio = []
#     #     for story in project_stories:
#     #         audio=story.get_story_audio()
#     #         project_audio.extend(audio)
#     #     return set(project_audio)
#
#     # def get_project_video(self):
#     #     """Return all video assets associated with items that are part of a project."""
#     #
#     #     # get all original stories associated with a project
#     #     project_stories = self.story_set.filter(original_story=True).all()
#     #     # get all video assets associated with those stories.
#     #     project_video = []
#     #     for story in project_stories:
#     #         videos=story.get_story_video()
#     #         project_video.extend(videos)
#     #     return set(project_video)
#
#     # TODO Delete
#     # def get_project_tasks(self):
#     #     """Return all tasks associated with a project."""
#     #     return self.task_set.all()
#
#     # def get_project_stories(self):
#     #     """Return all original stories associated with a project."""
#     #     return self.story_set.filter(original_story=True).all()
#
#     # def get_project_event_schedule(self):
#     #     """Return project events for a project.
#     #
#     #     Used for returning a single project's event schedule.
#     #     """
#     #
#     #     data = []
#     #
#     #     project = Project.objects.get(pk=self.id)
#     #
#     #     # gather schedule dates for all project events
#     #     if project.event_set.all():
#     #         for event in project.event_set.filter(event_type="Hosting"):
#     #             hosting_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             hosting_event_dict['id'] = event.id
#     #             hosting_event_dict['title'] = event.name
#     #             hosting_event_dict['event_date'] = item_date.isoformat()
#     #             hosting_event_dict['url'] = event.get_absolute_url()
#     #             hosting_event_dict['start'] = item_date.isoformat()
#     #             hosting_event_dict['end'] = item_date.isoformat()
#     #             hosting_event_dict['overlap'] = True
#     #             hosting_event_dict['all_day'] = False
#     #             hosting_event_dict['backgroundColor'] = '#3F51B5'
#     #             hosting_event_dict['textColor'] = 'fff'
#     #             hosting_event_dict['class'] = "calevent"
#     #
#     #             data.append(hosting_event_dict)
#     #
#     #         for event in project.event_set.filter(event_type="Reporting"):
#     #             reporting_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             reporting_event_dict['id'] = event.id
#     #             reporting_event_dict['title'] = event.name
#     #             reporting_event_dict['event_date'] = item_date.isoformat()
#     #             reporting_event_dict['url'] = event.get_absolute_url()
#     #             reporting_event_dict['start'] = item_date.isoformat()
#     #             reporting_event_dict['end'] = item_date.isoformat()
#     #             reporting_event_dict['overlap'] = True
#     #             reporting_event_dict['all_day'] = False
#     #             reporting_event_dict['backgroundColor'] = '#2196F3'
#     #             reporting_event_dict['textColor'] = 'fff'
#     #             reporting_event_dict['class'] = "calevent"
#     #
#     #             data.append(reporting_event_dict)
#     #
#     #         for event in project.event_set.filter(event_type="Administrative"):
#     #             administrative_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             administrative_event_dict['id'] = event.id
#     #             administrative_event_dict['title'] = event.name
#     #             administrative_event_dict['event_date'] = item_date.isoformat()
#     #             administrative_event_dict['url'] = event.get_absolute_url()
#     #             administrative_event_dict['start'] = item_date.isoformat()
#     #             administrative_event_dict['end'] = item_date.isoformat()
#     #             administrative_event_dict['overlap'] = True
#     #             administrative_event_dict['all_day'] = False
#     #             administrative_event_dict['backgroundColor'] = '#03A9F4'
#     #             administrative_event_dict['textColor'] = 'fff'
#     #             administrative_event_dict['class'] = "calevent"
#     #
#     #             data.append(administrative_event_dict)
#     #
#     #         for event in project.event_set.filter(event_type="Other"):
#     #             other_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             other_event_dict['id'] = event.id
#     #             other_event_dict['title'] = event.name
#     #             other_event_dict['event_date'] = item_date.isoformat()
#     #             other_event_dict['url'] = event.get_absolute_url()
#     #             other_event_dict['start'] = item_date.isoformat()
#     #             other_event_dict['end'] = item_date.isoformat()
#     #             other_event_dict['overlap'] = True
#     #             other_event_dict['all_day'] = False
#     #             other_event_dict['backgroundColor'] = '#00BCD4'
#     #             other_event_dict['textColor'] = 'fff'
#     #             other_event_dict['class'] = "calevent"
#     #
#     #             data.append(other_event_dict)
#     #
#     #     return data
#
#     # def get_project_schedule(self):
#     #     """Return all the relevant dates for a project.
#     #     Used for returning a single project's schedule.
#     #
#     #     Includes:
#     #     From story:
#     #         story_share_date
#     #         item due_edit
#     #         item run_date
#     #     From project:
#     #         event event_date
#     #         task due_date
#     #     """
#     #
#     #     data = []
#     #
#     #     project = Project.objects.get(pk=self.id)
#     #
#     #     # gather dates for story sharing and story items for a project
#     #     if project.story_set:
#     #         for story in project.story_set.all():
#     #             single_story_dates = story.get_story_items_schedule()
#     #             data.extend(single_story_dates)
#     #
#     #     # gather schedule dates for all story events
#     #     if project.event_set.all():
#     #         for event in project.event_set.filter(event_type="Hosting"):
#     #             hosting_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             hosting_event_dict['id'] = event.id
#     #             hosting_event_dict['title'] = event.name
#     #             hosting_event_dict['event_date'] = item_date.isoformat()
#     #             hosting_event_dict['url'] = event.get_absolute_url()
#     #             hosting_event_dict['start'] = item_date.isoformat()
#     #             hosting_event_dict['end'] = item_date.isoformat()
#     #             hosting_event_dict['overlap'] = True
#     #             hosting_event_dict['all_day'] = False
#     #             hosting_event_dict['backgroundColor'] = '#3F51B5'
#     #             hosting_event_dict['textColor'] = 'fff'
#     #             hosting_event_dict['class'] = "calevent"
#     #
#     #             data.append(hosting_event_dict)
#     #
#     #         for event in project.event_set.filter(event_type="Reporting"):
#     #             reporting_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             reporting_event_dict['id'] = event.id
#     #             reporting_event_dict['title'] = event.name
#     #             reporting_event_dict['event_date'] = item_date.isoformat()
#     #             reporting_event_dict['url'] = event.get_absolute_url()
#     #             reporting_event_dict['start'] = item_date.isoformat()
#     #             reporting_event_dict['end'] = item_date.isoformat()
#     #             reporting_event_dict['overlap'] = True
#     #             reporting_event_dict['all_day'] = False
#     #             reporting_event_dict['backgroundColor'] = '#2196F3'
#     #             reporting_event_dict['textColor'] = 'fff'
#     #             reporting_event_dict['class'] = "calevent"
#     #
#     #             data.append(reporting_event_dict)
#     #
#     #         for event in project.event_set.filter(event_type="Administrative"):
#     #             administrative_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             administrative_event_dict['id'] = event.id
#     #             administrative_event_dict['title'] = event.name
#     #             administrative_event_dict['event_date'] = item_date.isoformat()
#     #             administrative_event_dict['url'] = event.get_absolute_url()
#     #             administrative_event_dict['start'] = item_date.isoformat()
#     #             administrative_event_dict['end'] = item_date.isoformat()
#     #             administrative_event_dict['overlap'] = True
#     #             administrative_event_dict['all_day'] = False
#     #             administrative_event_dict['backgroundColor'] = '#03A9F4'
#     #             administrative_event_dict['textColor'] = 'fff'
#     #             administrative_event_dict['class'] = "calevent"
#     #
#     #             data.append(administrative_event_dict)
#     #
#     #         for event in project.event_set.filter(event_type="Other"):
#     #             other_event_dict = {}
#     #
#     #             item_date = event.event_date
#     #
#     #             other_event_dict['id'] = event.id
#     #             other_event_dict['title'] = event.name
#     #             other_event_dict['event_date'] = item_date.isoformat()
#     #             other_event_dict['url'] = event.get_absolute_url()
#     #             other_event_dict['start'] = item_date.isoformat()
#     #             other_event_dict['end'] = item_date.isoformat()
#     #             other_event_dict['overlap'] = True
#     #             other_event_dict['all_day'] = False
#     #             other_event_dict['backgroundColor'] = '#00BCD4'
#     #             other_event_dict['textColor'] = 'fff'
#     #             other_event_dict['class'] = "calevent"
#     #
#     #             data.append(other_event_dict)
#     #
#     #     # gather schedule dates for all story tasks
#     #     if project.task_set.all():
#     #         for task in project.task_set.all():
#     #             task_event_dict = {}
#     #
#     #             item_date = task.due_date
#     #
#     #             task_event_dict['id'] = task.id
#     #             task_event_dict['title'] = task.name
#     #             task_event_dict['due_date'] = item_date.isoformat()
#     #             task_event_dict['url'] = task.get_absolute_url()
#     #             task_event_dict['start'] = item_date.isoformat()
#     #             task_event_dict['end'] = item_date.isoformat()
#     #             task_event_dict['overlap'] = True
#     #             task_event_dict['all_day'] = False
#     #             task_event_dict['backgroundColor'] = '#7E57C2'
#     #             task_event_dict['textColor'] = 'fff'
#     #             task_event_dict['class'] = "calevent"
#     #
#     #             data.append(task_event_dict)
#     #
#     #     return data

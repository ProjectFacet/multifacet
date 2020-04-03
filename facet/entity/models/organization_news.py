# from django.db import models
#
# from base.models import BaseOrganization
# from base.models import Participant
#
# class NewsOrganization(BaseOrganization):
#     """ Media Organization.
#
#     A mews organization is a media or publishing entity. News organizations are created
#     and owned by one or more admin participants. They can be managed by multiple admin participants.
#     News organizations have many participants and serve as the owner of project and story content. News organizations
#     can create and manage Networks. Ownership of a news organization can be transferred
#     from one admin participant to another.
#     """
#
#     active = models.BooleanField(
#         default=True,
#         help_text='Whether the news organization is in active operations.'
#     )
#
#     mission_statement = models.TextField(
#         blank = True,
#         help_text = 'Statement of mission and goals of the news organization.'
#     )
#
#     list_publicly = models.BooleanField(
#         default=False,
#         help_text='Whether the news organization is listed publicly in discovery.',
#     )
#
#     # ----------------------------------------------------
#     # public visibility of business_structure
#     display_business_structure = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for business_structure.'
#     )
#
#     # Profile fields
#     NONPROFIT = 'Nonprofit - 501C3'
#     FOR_PROFIT = 'For profit'
#     B_CORP = 'B Corp'
#     COOPERATIVE = 'Cooperative'
#     DIRECT_OFFERING = 'Direct Offering'
#     HYBRID = 'Hybrid'
#     EMPLOYEE_OWNED = 'Employee Owned'
#     OTHER = 'Other'
#     BUSINESS_TYPE_CHOICES = (
#         (NONPROFIT, 'Nonprofit'),
#         (FOR_PROFIT, 'For profit'),
#         (B_CORP, 'B Corporation'),
#         (COOPERATIVE, 'Cooperative'),
#         (DIRECT_OFFERING, 'Direct Offering'),
#         (HYBRID, 'Hybrid'),
#         (EMPLOYEE_OWNED, 'Employee Owned'),
#         (OTHER, 'Other'),
#     )
#
#     business_structure = models.CharField(
#         max_length=50,
#         choices=BUSINESS_TYPE_CHOICES,
#         help_text='Business structure of the news organization.',
#         blank=True,
#     )
#
#     # ----------------------------------------------------
#     # public visibility of platform_
#     display_platforms = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for platform_ options.'
#     )
#
#     # platforms
#     platform_print = models.BooleanField(
#         default=False,
#         help_text='News Organization publishes in print.',
#     )
#
#     platform_online = models.BooleanField(
#         default=False,
#         help_text='News Organization publishes online.',
#     )
#
#     platform_social = models.BooleanField(
#         default=False,
#         help_text='News Organization publishes content on social platforms.',
#     )
#
#     platform_network_tv = models.BooleanField(
#         default=False,
#         help_text='News Organization airs on network television.',
#     )
#
#     platform_cable_tv = models.BooleanField(
#         default=False,
#         help_text='News Organization airs on cable television.',
#     )
#
#     platform_radio = models.BooleanField(
#         default=False,
#         help_text='News Organization airs on radio.',
#     )
#
#     platform_podcast = models.BooleanField(
#         default=False,
#         help_text='News Organization produces podcasts.',
#     )
#
#     platform_newsletter = models.BooleanField(
#         default=False,
#         help_text='News Organization publishes newsletters.',
#     )
#
#     platform_streaming_video = models.BooleanField(
#         default=False,
#         help_text='News Organization content airs on streaming video.',
#     )
#
#     # ----------------------------------------------------
#     # public visibility of audience
#     display_audience = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for audience.'
#     )
#
#     audience = models.CharField(
#         max_length=255,
#         blank=True,
#         help_text='Description of primary audiences.'
#     )
#
#     # ----------------------------------------------------
#     # public visibility of ownership
#     display_ownership = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for ownership.'
#     )
#
#     ownership = models.TextField(
#         blank=True,
#         help_text='What or who owns the news organization.'
#     )
#
#     # ----------------------------------------------------
#     # public visibility of business_model
#     display_business_model = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for business_model.'
#     )
#
#     business_model = models.TextField(
#         blank=True,
#         help_text='What are the sources of support for the news organization.'
#     )
#
#     # ----------------------------------------------------
#     # public visibility of unionization
#     display_unionization = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for unionization.'
#     )
#
#     unionization = models.CharField(
#         max_length=255,
#         blank=True,
#         help_text='Is any part of the news organization workforce unionized.'
#     )
#
#     # ----------------------------------------------------
#     # public visibility of diversity
#     display_diversity = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for diversity.'
#     )
#
#     diversity = models.TextField(
#         help_text="The makeup of the news organization and any programs or efforts to help ensure diversity in staffing.",
#         blank=True,
#     )
#
#     # ----------------------------------------------------
#     # public visibility of strengths
#     display_strengths = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for strengths.'
#     )
#
#     strengths = models.TextField(
#         help_text="Any special skills or strengths this newsroom has.",
#         blank=True,
#     )
#
#     # ----------------------------------------------------
#     # public visibility of partner_qualities
#     display_partner_qualities = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for partner_qualities.'
#     )
#
#     partner_qualities = models.TextField(
#         help_text="What about this organization makes it a good collaborative partner.",
#         blank=True,
#     )
#
#     # ----------------------------------------------------
#     # public visibility of best_coverage
#     display_best_coverage = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for best_coverage.'
#     )
#
#     best_coverage = models.TextField(
#         help_text="What coverage has this organization been involved in that the newsroom is proud of.",
#         blank=True,
#     )
#
#     # ----------------------------------------------------
#     # public visibility of collab_experience
#     display_collab_experience = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for collab_experience.'
#     )
#
#     collab_experience = models.TextField(
#         blank=True,
#         help_text='Has the news organization collaborated before and how often.'
#     )
#
#     # ----------------------------------------------------
#     # public visibility of seeking_collabs
#     display_seeking_collabs = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for seeking_collabs.'
#     )
#
#     seeking_collabs = models.BooleanField(
#         default=False,
#         help_text='Actively seeking collaborative projects to participate in.'
#     )
#
#     # ----------------------------------------------------
#     # public visibility of seeking_partners
#     display_seeking_partners = models.BooleanField(
#         default=False,
#         help_text = 'Publicly display values for seeking_partners.'
#     )
#
#     seeking_partners = models.BooleanField(
#         default=False,
#         help_text='Actively seeking partners for a specific project.'
#     )
#
#     class Meta:
#         verbose_name = 'News Organization'
#         verbose_name_plural = "News Organizations"
#
#     def __str__(self):
#         return self.name
#
#     # def get_absolute_url(self):
#     #     return reverse('org_detail', kwargs={'pk': self.id})
#
#     @property
#     def description(self):
#         return "{description}".format(description=self.description)
#
#     @property
#     def search_title(self):
#         return self.name
#
#     @property
#     def type(self):
#         return "News Organization"
#
#     # def get_org_participants(self):
#     #     """ Return queryset of all participants in a news organization.
#     #
#     #     Used for news organization dashboards, team views and context processors.
#     #     """
#     #     return self.participant_set.all()
#
#     # def get_org_networks(self):
#     #     """ Return list of all the networks that a news organization is connected to as
#     #     owner or member of.
#     #
#     #     Used for dashboard, network dashboards and network content.
#     #     """
#     #
#     #     from . import Network
#     #
#     #     all_org_networks = Network.objects.filter(Q(Q(owner_organization=self) | Q(organizations=self)))
#     #
#     #     # not necessary but leaving in for now, check to make sure unique list of networks
#     #     organization_networks = all_org_networks.distinct()
#     #
#     #     return organization_networks
#
#     # def get_org_network_content(self):
#     #     """Return queryset of content shared with any network a news organization is a member of excluding their own content."""
#     #
#     #     # FIXME: does this actually exclude their own content? - Joel
#     #
#     #     from . import Story
#     #
#     #     networks = self.get_org_networks()
#     #     network_content = Story.objects.filter(share_with__in=networks).select_related('newsorganization')
#     #
#     #     return network_content
#
#     # def get_org_copied_content(self):
#     #     """Returns queryset of content that a news organization has picked up from
#     #     a network partner."""
#     #
#     #     from . import StoryCopyDetail
#     #     from . import Story
#     #
#     #     copyrecords = StoryCopyDetail.objects.exclude(original_org=self)
#     #     org_copied_content = [record.original_story for record in copyrecords]
#     #
#     #     return org_copied_content
#
#     # # formerly get_org_collaborators
#     # def get_org_collaborators_vocab(self):
#     #     """ Return list of all organizations that are members of the same networks as self.
#     #
#     #     Used to for selecting organizations to collaborate with and for displaying partners
#     #     in team dashboard. Also used to create get_participant_contact_list_vocab.
#     #     """
#     #
#     #     # get list of networks that an org is a member of
#     #     networks = self.get_org_networks()
#     #     # get list of news organizations that are owners of any of those networks
#     #     # get list of news organizations that are members of any of those networks
#     #     # exclude self org
#     #     unique_collaborators = NewsOrganization.objects.filter(Q(network_organization__in=networks) | Q(id__in=networks.values('owner_organization'))).exclude(id=self.id)
#     #
#     #     return unique_collaborators
#
#     # def get_org_image_library(self):
#     #     """ Return list of all images associated with a news organization.
#     #
#     #     Used to display images in media gallery.
#     #     """
#     #     return self.imageasset_set.all()
#
#     # def get_org_document_library(self):
#     #     """ Return list of all documents associated with a news organization.
#     #
#     #     Used to display documents in media gallery.
#     #     """
#     #     return self.documentasset_set.all()
#
#     # def get_org_audio_library(self):
#     #     """ Return list of all audio files associated with a news organization.
#     #
#     #     Used to display audio in media gallery.
#     #     """
#     #     return self.audioasset_set.all()
#
#     # def get_org_video_library(self):
#     #     """ Return list of all video files associated with a news organization.
#     #
#     #     Used to display videos in media gallery.
#     #     """
#     #     return self.videoasset_set.all()
#
#     # def get_org_recent_media(self):
#     #     """ Return 24 most recently uploaded media asset files."""
#     #
#     #     # FIXME how to best query for the 24 most recent media assets across types.
#     #     images = self.imageasset_set.all().order_by("-creation_date")[:12]
#     #     docs = self.documentasset_set.all().order_by("-creation_date")[:12]
#     #     audio = self.audioasset_set.all().order_by("-creation_date")[:12]
#     #     video = self.videoasset_set.all().order_by("-creation_date")[:12]
#     #     recentmedia = []
#     #     recentmedia.extend(images)
#     #     recentmedia.extend(docs)
#     #     recentmedia.extend(audio)
#     #     recentmedia.extend(video)
#     #     print "RECENT MEDIA: ", recentmedia
#     #
#     #     return recentmedia
#
#     # def get_org_simple_image_library(self):
#     #     """ Return queryset of all simple images associated with a news organization."""
#     #
#     #     return self.simpleimage_set.all()
#
#     # def get_org_simple_document_library(self):
#     #     """ Return queryset of all simple documents associated with an organizaiton."""
#     #
#     #     return self.simpledocument_set.all()
#
#     # def get_org_simple_audio_library(self):
#     #     """ Return queryset of all simple audio associated with a news organization."""
#     #
#     #     return self.simpleaudio_set.all()
#
#     # def get_org_simple_video_library(self):
#     #     """ Return queryset of all simple video associated with a news organization."""
#     #
#     #     return self.simplevideo_set.all()
#
#     # def get_org_simple_asset_library(self):
#     #     """ Return organization simple assets."""
#     #
#     #     recent_internal_assets = []
#     #     simple_images = self.simpleimage_set.all().order_by("-creation_date")[:12]
#     #     simple_documents = self.simpledocument_set.all().order_by("-creation_date")[:12]
#     #     simple_audio = self.simpleaudio_set.all().order_by("-creation_date")[:12]
#     #     simple_video = self.simplevideo_set.all().order_by("-creation_date")[:12]
#     #     recent_internal_assets.extend(simple_images)
#     #     recent_internal_assets.extend(simple_documents)
#     #     recent_internal_assets.extend(simple_audio)
#     #     recent_internal_assets.extend(simple_video)
#     #
#     #     return recent_internal_assets
#
#     # def get_org_participant_comments(self):
#     #     """Retrieve all the comments associated with participants of a news organization.
#     #
#     #     Effectively 'all' comments for a news organization. Used in participant inbox
#     #     to display streams of all comments.
#     #     """
#     #
#     #     from . import Comment
#     #
#     #     participants = self.get_org_participants()
#     #     org_participant_comments = Comment.objects.filter(Q(participant__in=participants))
#     #
#     #     return org_participant_comments
#
#     # def get_org_comments(self):
#     #     """Retrieve all organization comments.
#     #
#     #     Used to display all organization comments in dashboard and inbox.
#     #     """
#     #
#     #     from . import Comment
#     #     organization_comments = Comment.objects.filter(discussion__discussion_type='ORG', participant__organization=self)
#     #     return organization_comments
#
#     # def get_network_comments(self):
#     #     """Retrieve all comments for networks a news organization is a member of.
#     #
#     #     Used to display all network comments in dashboard and inbox.
#     #     """
#     #
#     #     from . import Comment
#     #
#     #     networks = self.get_org_networks()
#     #     network_discussions = [network.discussion for network in networks]
#     #     network_comments = Comment.objects.filter(discussion__in=network_discussions)
#     #     return network_comments
#
#     # def get_project_comments(self):
#     #     """Retrieve all comments for projects belonging to a news organization.
#     #
#     #     Used to display all project comments in dashboard and inbox."""
#     #
#     #     from . import Project, Comment
#     #
#     #     # TODO include projects that are collaborative
#     #     org_projects = self.project_organization.all()
#     #     project_discussions = [project.discussion for project in org_projects]
#     #     project_comments = Comment.objects.filter(discussion__in=project_discussions)
#     #     return project_comments
#
#     # def get_story_comments(self):
#     #     """Retrieve all comments for stories belonging to a news organization.
#     #
#     #     Used to display all story comments in dashboard and inbox.
#     #     """
#     #
#     #     from . import Story, Comment
#     #
#     #     # TODO include stories that are collaborative
#     #     org_stories = Story.objects.filter(organization=self)
#     #     story_discussions = [story.discussion for story in org_stories]
#     #     story_comments = Comment.objects.filter(discussion__in=story_discussions)
#     #     return story_comments
#
#     # def get_item_comments(self):
#     #     """Retrieve all comments for items belonging to stories of a news organization.
#     #
#     #     Used to display all item comments in dashboard and inbox.
#     #     """
#     #     from .item import Item
#     #     from .discussion import Comment
#     #     # WJB XXX: this seems inefficient, we should reduce to discussion fields on orig
#     #     # querysets
#     #
#     #     # TODO include items on stories that are collaborative
#     #     org_items = self.item_set.all()
#     #     item_discussions = [item.discussion for item in org_items]
#     #     item_comments = Comment.objects.filter(discussion__in=item_discussions)
#     #     return item_comments
#
#     # def get_org_collaborative_content(self):
#     #     """ Return list of all content that an org is a collaborator on.
#     #
#     #     All of the collaborative content a news organization is participating in
#     #     is displaying in a collaborative content dashboard.
#     #     """
#     #
#     #     from .story import Story
#     #     org_collaborative_content = []
#     #     external_stories = Story.objects.filter(Q(collaborate_with=self))
#     #     internal_stories = self.story_set.filter(Q(organization=self) & Q(collaborate=True))
#     #     org_collaborative_content.extend(external_stories)
#     #     org_collaborative_content.extend(internal_stories)
#     #     return org_collaborative_content
#
#     # def get_org_external_collaborations(self):
#     #     """ Return all content from partner orgs that a news organization is a
#     #     collaborator on.
#     #     """
#     #
#     #     from . import Project
#     #     from . import Story
#     #     external_collaborative_content = []
#     #     external_projects = Project.objects.filter(Q(collaborate_with=self))
#     #     external_stories = Story.objects.filter(Q(collaborate_with=self))
#     #     external_collaborative_content.extend(external_projects)
#     #     external_collaborative_content.extend(external_stories)
#     #     return external_collaborative_content
#
#     # def get_org_internal_collaborations(self):
#     #     """ Return all content that a news organization owns that is a collaboration
#     #     with partner organizations.
#     #     """
#     #
#     #     internal_collaborative_content = []
#     #     internal_projects = self.project_set.filter(Q(collaborate=True))
#     #     internal_stories = self.story_set.filter(Q(collaborate=True))
#     #     internal_collaborative_content.extend(internal_projects)
#     #     internal_collaborative_content.extend(internal_stories)
#     #     return internal_collaborative_content
#
#     # def get_org_stories_running_today(self):
#     #     """Return list of content scheduled to run today.
#     #
#     #     Used to display content scheduled to run on any given day
#     #     on the primary dashboard.
#     #     """
#     #
#     #     from . import Item
#     #
#     #     #FIXME today, tomorrow if off by one day (hacky fix in place)
#     #     # establish timeliness of content
#     #     today = timezone.now().date() - timedelta(1)
#     #     tomorrow = timezone.now().date()
#     #     today_start = datetime.combine(today, time())
#     #     today_end = datetime.combine(tomorrow, time())
#     #
#     #     # items where run_date=today
#     #     running_today = Item.objects.filter(run_date__range=(today_start, today_end), organization=self)
#     #
#     #     return running_today
#
#     # def get_org_stories_due_for_edit_today(self):
#     #     """Return list of content scheduled for edit today.
#     #
#     #     Used to display content scheduled for edit on any given day
#     #     on the primary dashboard.
#     #     """
#     #
#     #     from .item import Item
#     #
#     #     #FIXME today, tomorrow if off by one day (hacky fix in place)
#     #     # establish timeliness of content
#     #     today = timezone.now().date() - timedelta(1)
#     #     tomorrow = timezone.now().date()
#     #     today_start = datetime.combine(today, time())
#     #     today_end = datetime.combine(tomorrow, time())
#     #
#     #     edit_today = Item.objects.filter(due_edit__range=(today_start, today_end), organization=self)
#     #
#     #     return edit_today
#
#     # def get_org_projects(self):
#     #     """Return queryset of projects associated with a news organization for
#     #     use in PlatformAccount forms.
#     #     """
#     #
#     #     from . import Project
#     #     projects = []
#     #     networks = NewsOrganization.get_org_networks(self)
#     #     network_projects = Project.objects.filter(share_with__in=networks)
#     #     org_projects = Project.objects.filter(organization=self)
#     #     projects.extend(network_projects)
#     #     projects.extend(org_projects)
#     #     return projects
#
#     # def get_org_content_tasks(self):
#     #     """Return all the tasks associated with projects, stories, or events.
#     #
#     #     This includes items from content that is collaborative.
#     #     """
#     #
#     #     return self.task_set.all()
#
#     # def get_org_events(self):
#     #     """Return all the events associated with the org or org content.
#     #
#     #     This includes items from content that is collaborative.
#     #     """
#     #     return self.event_set.all()
#
#     # def get_org_searchable_comments(self):
#     #     """Return all the comments that should appear in search results.
#     #
#     #     This includes comments from items that are collaborative.
#     #     """
#     #     return self.get_org_participant_comments()
#
#     # def get_org_searchable_notes(self):
#     #     """Return all the notes that should appear in search results.
#     #     This includes notes from items that are collaborative."""
#     #
#     #     return Note.objects.filter(participant__organization=self).exclude(note_type='Participant')
#
#     # def get_org_searchable_content(self):
#     #     """Return queryset of all objects that can be searched by a participant."""
#     #
#     #     from .projects import Project
#     #     from .story import Story
#     #     from .item import Item
#     #
#     #     #additional required info
#     #     networks = self.get_org_networks()
#     #
#     #     searchable_objects = []
#     #
#     #     projects = Project.objects.filter(Q(Q(organization=self) | Q(collaborate_with=self)))
#     #     stories = Story.objects.filter(Q(Q(organization=self) | Q(collaborate_with=self)))
#     #     items = Item.objects.filter(Q(organization=self))
#     #     imageassets = self.imageasset_set.all()
#     #     documentassets = self.documentasset_set.all()
#     #     audioassets = self.audioasset_set.all()
#     #     tasks = self.get_org_content_tasks()
#     #     events = self.get_org_events()
#     #     comments = self.get_org_searchable_comments()
#     #     notes = self.get_org_searchable_notes()
#     #
#     #     searchable_objects.append(projects)
#     #     searchable_objects.append(stories)
#     #     searchable_objects.append(items)
#     #     searchable_objects.append(imageassets)
#     #     searchable_objects.append(documentassets)
#     #     searchable_objects.append(audioassets)
#     #     searchable_objects.append(tasks)
#     #     searchable_objects.append(events)
#     #     searchable_objects.append(notes)
#     #     searchable_objects.append(comments)
#     #
#     #     return searchable_objects
#
#     # def get_org_itemtemplates(self):
#     #     """Return queryset of item templates that should be available of org items."""
#     #
#     #     from . import ItemTemplate
#     #
#     #     return ItemTemplate.objects.filter(Q(organization_id__isnull=True) | Q(organization=self) & Q(is_active=True))
#
#
#
#
# # @receiver(post_save, sender=Organization)
# # def add_discussion(sender, instance, **kwargs):
# #     from . import Discussion
# #     from . import NewsOrganizationPublicProfile
# #
# #     if not instance.discussion:
# #         instance.discussion = Discussion.objects.create_discussion("ORG")
# #     if not instance.public_profile:
# #         instance.public_profile = NewsOrganizationPublicProfile.objects.create_public_profile()
# #         instance.save()

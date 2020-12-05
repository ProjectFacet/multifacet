from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.models import BaseOrganization, Participant
# from editorial.models import Item

class NewsOrganization(BaseOrganization):
    """ Media Organization.

    A news organization is a media or publishing entity. News organizations are created
    and owned by one or more admin participants. They can be managed by multiple admin participants.
    News organizations have many participants and serve as the owner of project and story content. News organizations
    can create and manage Networks. Ownership of a news organization can be transferred
    from one admin participant to another.
    """

    active = models.BooleanField(
        default=True,
        help_text='Whether the news organization is in active operations.'
    )

    mission_statement = models.TextField(
        blank = True,
        help_text = 'Statement of mission and goals of the news organization.'
    )

    list_publicly = models.BooleanField(
        default=False,
        help_text='Whether the news organization is listed publicly in discovery.',
    )

    # ----------------------------------------------------
    # public visibility of business_structure
    display_business_structure = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for business_structure.'
    )

    # Profile fields
    NONPROFIT = 'Nonprofit - 501c3'
    FOR_PROFIT = 'For profit'
    B_CORP = 'B Corp'
    COOPERATIVE = 'Cooperative'
    DIRECT_OFFERING = 'Direct Offering'
    HYBRID = 'Hybrid'
    EMPLOYEE_OWNED = 'Employee Owned'
    OTHER = 'Other'
    BUSINESS_TYPE_CHOICES = (
        (NONPROFIT, 'Nonprofit'),
        (FOR_PROFIT, 'For profit'),
        (B_CORP, 'B Corporation'),
        (COOPERATIVE, 'Cooperative'),
        (DIRECT_OFFERING, 'Direct Offering'),
        (HYBRID, 'Hybrid'),
        (EMPLOYEE_OWNED, 'Employee Owned'),
        (OTHER, 'Other'),
    )

    business_structure = models.CharField(
        max_length=50,
        choices=BUSINESS_TYPE_CHOICES,
        help_text='Business structure of the news organization.',
        blank=True,
    )

    # ----------------------------------------------------
    # public visibility of platform_
    display_platforms = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for platform_ options.'
    )

    # platforms
    platform_print = models.BooleanField(
        default=False,
        help_text='News Organization publishes in print.',
    )

    platform_online = models.BooleanField(
        default=False,
        help_text='News Organization publishes online.',
    )

    platform_social = models.BooleanField(
        default=False,
        help_text='News Organization publishes content on social platforms.',
    )

    platform_network_tv = models.BooleanField(
        default=False,
        help_text='News Organization airs on network television.',
    )

    platform_cable_tv = models.BooleanField(
        default=False,
        help_text='News Organization airs on cable television.',
    )

    platform_public_radio = models.BooleanField(
        default=False,
        help_text='News Organization airs on public radio.',
    )

    platform_commercial_radio = models.BooleanField(
        default=False,
        help_text='News Organization airs on commercial radio.',
    )

    platform_community_radio = models.BooleanField(
        default=False,
        help_text='News Organization airs on community radio.',
    )

    platform_podcast = models.BooleanField(
        default=False,
        help_text='News Organization produces podcasts.',
    )

    platform_newsletter = models.BooleanField(
        default=False,
        help_text='News Organization publishes newsletters.',
    )

    platform_streaming_video = models.BooleanField(
        default=False,
        help_text='News Organization content airs on streaming video.',
    )

    # ----------------------------------------------------
    # public visibility of audience
    display_audience = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for audience.'
    )

    audience = models.CharField(
        max_length=255,
        blank=True,
        help_text='Description of primary audiences.'
    )

    # ----------------------------------------------------
    # public visibility of ownership
    display_ownership = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for ownership.'
    )

    ownership = models.TextField(
        blank=True,
        help_text='What or who owns the news organization.'
    )

    # ----------------------------------------------------
    # public visibility of business_model
    display_business_model = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for business_model.'
    )

    business_model = models.TextField(
        blank=True,
        help_text='What are the sources of support for the news organization.'
    )

    # ----------------------------------------------------
    # public visibility of unionization
    display_unionization = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for unionization.'
    )

    unionization = models.CharField(
        max_length=255,
        blank=True,
        help_text='Is any part of the news organization workforce unionized.'
    )

    # ----------------------------------------------------
    # public visibility of diversity
    display_diversity = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for diversity.'
    )

    diversity = models.TextField(
        help_text="The makeup of the news organization and any programs or efforts to help ensure diversity in staffing.",
        blank=True,
    )

    # ----------------------------------------------------
    # public visibility of strengths
    display_strengths = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for strengths.'
    )

    strengths = models.TextField(
        help_text="Any special skills or strengths this newsroom has.",
        blank=True,
    )

    # ----------------------------------------------------
    # public visibility of partner_qualities
    display_partner_qualities = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for partner_qualities.'
    )

    partner_qualities = models.TextField(
        help_text="What about this organization makes it a good collaborative partner.",
        blank=True,
    )

    # ----------------------------------------------------
    # public visibility of best_coverage
    display_best_coverage = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for best_coverage.'
    )

    best_coverage = models.TextField(
        help_text="What coverage has this organization been involved in that the newsroom is proud of.",
        blank=True,
    )

    # ----------------------------------------------------
    # public visibility of collab_experience
    display_collab_experience = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for collab_experience.'
    )

    collab_experience = models.TextField(
        blank=True,
        help_text='Has the news organization collaborated before and how often.'
    )

    # ----------------------------------------------------
    # public visibility of seeking_collabs
    display_seeking_collabs = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for seeking_collabs.'
    )

    seeking_collabs = models.BooleanField(
        default=False,
        help_text='Actively seeking collaborative projects to participate in.'
    )

    # ----------------------------------------------------
    # public visibility of seeking_partners
    display_seeking_partners = models.BooleanField(
        default=False,
        help_text = 'Publicly display values for seeking_partners.'
    )

    seeking_partners = models.BooleanField(
        default=False,
        help_text='Actively seeking partners for a specific project.'
    )

    class Meta:
        verbose_name = 'News Organization'
        verbose_name_plural = "News Organizations"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('entity:organization_news_detail', kwargs={'pk': self.id})

    @property
    def description(self):
        return "{description}".format(description=self.description)

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "News Organization"


    def get_staff_team(self):
        """Return participants of an organization."""

        return [staffjournalist.participant for staffjournalist in self.staffjournalist_set.all()]


    def get_freelance_team(self):
        """Return freelancers associated with an organization."""

        return [freelancejournalist.participant for freelancejournalist in self.freelanceraffiliationrecord_set.all()]


    def get_networks(self):
        """Retrieve networks that the newsorganization manages or is a member of."""

        return NewsOrganizationNetwork.objects.filter(Q(Q(entity_owner=self.entity_owner_profile) | Q(member=self.network_member_profile)))


    def get_partner_vocab(self):
        """
        Returns partner_profiles of networks, entities and participents eligible for partnering.
        Any Network the NewsOrganization is a member or owner of.
        Any connections of the NewsOrganization.
        """

        connections_and_networks = []
        connections = self.connections
        networks = NewsOrganization.get_networks(self)
        network_partner_profiles = [network.partner_profile for network in networks]
        connections_and_networks.extend(connections)
        connections_and_networks.extend(network_partner_profiles)
        return connections_and_networks


    def get_projects(self):
        """Retrieve projects owned by a news organization."""

        return Project.objects.filter(entity_owner=self.entity_owner_profile)


    def get_collaborative_projects(self):
        """Retrieve collaborative projects owned by another entity but partnered
        on."""

        return Project.objects.filter(partner_with=self.partner_profile)


    def get_item_templates(self):
        """Return queryset of item templates that should be available."""

        from editorial.models import ItemTemplate

        return ItemTemplate.objects.filter(Q(sitewide=True) | Q(entity_owner=self.entity_owner_profile) & Q(is_active=True))


    def get_image_library(self):
        """Retrieve appropriate image library."""

        return ImageAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner

    def get_document_library(self):
        """Retrieve appropriate document library."""

        return DocumentAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner

    def get_audio_library(self):
        """Retrieve appropriate audio library."""

        return AudioAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner

    def get_video_library(self):
        """Retrieve appropriate video library."""

        return VideoAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner



    # def get_org_participants(self):
    #     """ Return queryset of all participants in a news organization.
    #
    #     Used for news organization dashboards, team views and context processors.
    #     """
    #     return self.participant_set.all()

    # def get_org_networks(self):
    #     """ Return list of all the networks that a news organization is connected to as
    #     owner or member of.
    #
    #     Used for dashboard, network dashboards and network content.
    #     """
    #
    #     from . import Network
    #
    #     all_org_networks = Network.objects.filter(Q(Q(owner_organization=self) | Q(organizations=self)))
    #
    #     # not necessary but leaving in for now, check to make sure unique list of networks
    #     organization_networks = all_org_networks.distinct()
    #
    #     return organization_networks

    # def get_org_network_content(self):
    #     """Return queryset of content shared with any network a news organization is a member of excluding their own content."""
    #
    #     # FIXME: does this actually exclude their own content? - Joel
    #
    #     from . import Story
    #
    #     networks = self.get_org_networks()
    #     network_content = Story.objects.filter(share_with__in=networks).select_related('newsorganization')
    #
    #     return network_content

    def get_copied_content(self):
        """Returns queryset of content picked up from a partner."""

        from . import StoryCopyDetail
        from . import Story

        copyrecords = StoryCopyDetail.objects.filter(partner=self.partner_profile)
        copied_content = [record.original_story for record in copyrecords]

        return copied_content

    # # formerly get_org_collaborators
    # def get_org_collaborators_vocab(self):
    #     """ Return list of all organizations that are members of the same networks as self.
    #
    #     Used to for selecting organizations to collaborate with and for displaying partners
    #     in team dashboard. Also used to create get_participant_contact_list_vocab.
    #     """
    #
    #     # get list of networks that an org is a member of
    #     networks = self.get_org_networks()
    #     # get list of news organizations that are owners of any of those networks
    #     # get list of news organizations that are members of any of those networks
    #     # exclude self org
    #     unique_collaborators = NewsOrganization.objects.filter(Q(network_organization__in=networks) | Q(id__in=networks.values('owner_organization'))).exclude(id=self.id)
    #
    #     return unique_collaborators

    # def get_org_image_library(self):
    #     """ Return list of all images associated with a news organization.
    #
    #     Used to display images in media gallery.
    #     """
    #     return self.imageasset_set.all()

    # def get_org_document_library(self):
    #     """ Return list of all documents associated with a news organization.
    #
    #     Used to display documents in media gallery.
    #     """
    #     return self.documentasset_set.all()

    # def get_org_audio_library(self):
    #     """ Return list of all audio files associated with a news organization.
    #
    #     Used to display audio in media gallery.
    #     """
    #     return self.audioasset_set.all()

    # def get_org_video_library(self):
    #     """ Return list of all video files associated with a news organization.
    #
    #     Used to display videos in media gallery.
    #     """
    #     return self.videoasset_set.all()

    # def get_org_recent_media(self):
    #     """ Return 24 most recently uploaded media asset files."""
    #
    #     # FIXME how to best query for the 24 most recent media assets across types.
    #     images = self.imageasset_set.all().order_by("-creation_date")[:12]
    #     docs = self.documentasset_set.all().order_by("-creation_date")[:12]
    #     audio = self.audioasset_set.all().order_by("-creation_date")[:12]
    #     video = self.videoasset_set.all().order_by("-creation_date")[:12]
    #     recentmedia = []
    #     recentmedia.extend(images)
    #     recentmedia.extend(docs)
    #     recentmedia.extend(audio)
    #     recentmedia.extend(video)
    #     print "RECENT MEDIA: ", recentmedia
    #
    #     return recentmedia

    # def get_org_internal_image_library(self):
    #     """ Return queryset of all internal images associated with a news organization."""
    #
    #     return self.internalimage_set.all()

    # def get_org_internal_document_library(self):
    #     """ Return queryset of all internal documents associated with an organizaiton."""
    #
    #     return self.internaldocument_set.all()

    # def get_org_internal_audio_library(self):
    #     """ Return queryset of all internal audio associated with a news organization."""
    #
    #     return self.internalaudio_set.all()

    # def get_org_internal_video_library(self):
    #     """ Return queryset of all internal video associated with a news organization."""
    #
    #     return self.internalvideo_set.all()

    # def get_org_internal_asset_library(self):
    #     """ Return organization internal assets."""
    #
    #     recent_internal_assets = []
    #     internal_images = self.internalimage_set.all().order_by("-creation_date")[:12]
    #     internal_documents = self.internaldocument_set.all().order_by("-creation_date")[:12]
    #     internal_audio = self.internalaudio_set.all().order_by("-creation_date")[:12]
    #     internal_video = self.internalvideo_set.all().order_by("-creation_date")[:12]
    #     recent_internal_assets.extend(internal_images)
    #     recent_internal_assets.extend(internal_documents)
    #     recent_internal_assets.extend(internal_audio)
    #     recent_internal_assets.extend(internal_video)
    #
    #     return recent_internal_assets

    # def get_org_participant_comments(self):
    #     """Retrieve all the comments associated with participants of a news organization.
    #
    #     Effectively 'all' comments for a news organization. Used in participant inbox
    #     to display streams of all comments.
    #     """
    #
    #     from . import Comment
    #
    #     participants = self.get_org_participants()
    #     org_participant_comments = Comment.objects.filter(Q(participant__in=participants))
    #
    #     return org_participant_comments

    # def get_org_comments(self):
    #     """Retrieve all organization comments.
    #
    #     Used to display all organization comments in dashboard and inbox.
    #     """
    #
    #     from . import Comment
    #     organization_comments = Comment.objects.filter(discussion__discussion_type='ORG', participant__organization=self)
    #     return organization_comments

    # def get_network_comments(self):
    #     """Retrieve all comments for networks a news organization is a member of.
    #
    #     Used to display all network comments in dashboard and inbox.
    #     """
    #
    #     from . import Comment
    #
    #     networks = self.get_org_networks()
    #     network_discussions = [network.discussion for network in networks]
    #     network_comments = Comment.objects.filter(discussion__in=network_discussions)
    #     return network_comments

    # def get_project_comments(self):
    #     """Retrieve all comments for projects belonging to a news organization.
    #
    #     Used to display all project comments in dashboard and inbox."""
    #
    #     from . import Project, Comment
    #
    #     # TODO include projects that are collaborative
    #     org_projects = self.project_organization.all()
    #     project_discussions = [project.discussion for project in org_projects]
    #     project_comments = Comment.objects.filter(discussion__in=project_discussions)
    #     return project_comments

    # def get_story_comments(self):
    #     """Retrieve all comments for stories belonging to a news organization.
    #
    #     Used to display all story comments in dashboard and inbox.
    #     """
    #
    #     from . import Story, Comment
    #
    #     # TODO include stories that are collaborative
    #     org_stories = Story.objects.filter(organization=self)
    #     story_discussions = [story.discussion for story in org_stories]
    #     story_comments = Comment.objects.filter(discussion__in=story_discussions)
    #     return story_comments

    # def get_item_comments(self):
    #     """Retrieve all comments for items belonging to stories of a news organization.
    #
    #     Used to display all item comments in dashboard and inbox.
    #     """
    #     from .item import Item
    #     from .discussion import Comment
    #     # WJB XXX: this seems inefficient, we should reduce to discussion fields on orig
    #     # querysets
    #
    #     # TODO include items on stories that are collaborative
    #     org_items = self.item_set.all()
    #     item_discussions = [item.discussion for item in org_items]
    #     item_comments = Comment.objects.filter(discussion__in=item_discussions)
    #     return item_comments

    # def get_org_collaborative_content(self):
    #     """ Return list of all content that an org is a collaborator on.
    #
    #     All of the collaborative content a news organization is participating in
    #     is displaying in a collaborative content dashboard.
    #     """
    #
    #     from .story import Story
    #     org_collaborative_content = []
    #     external_stories = Story.objects.filter(Q(partner_with=self))
    #     internal_stories = self.story_set.filter(Q(organization=self) & Q(collaborate=True))
    #     org_collaborative_content.extend(external_stories)
    #     org_collaborative_content.extend(internal_stories)
    #     return org_collaborative_content

    # def get_org_external_collaborations(self):
    #     """ Return all content from partner orgs that a news organization is a
    #     collaborator on.
    #     """
    #
    #     from . import Project
    #     from . import Story
    #     external_collaborative_content = []
    #     external_projects = Project.objects.filter(Q(partner_with=self))
    #     external_stories = Story.objects.filter(Q(partner_with=self))
    #     external_collaborative_content.extend(external_projects)
    #     external_collaborative_content.extend(external_stories)
    #     return external_collaborative_content

    # def get_org_internal_collaborations(self):
    #     """ Return all content that a news organization owns that is a collaboration
    #     with partner organizations.
    #     """
    #
    #     internal_collaborative_content = []
    #     internal_projects = self.project_set.filter(Q(collaborate=True))
    #     internal_stories = self.story_set.filter(Q(collaborate=True))
    #     internal_collaborative_content.extend(internal_projects)
    #     internal_collaborative_content.extend(internal_stories)
    #     return internal_collaborative_content

    # def get_org_stories_running_today(self):
    #     """Return list of content scheduled to run today.
    #
    #     Used to display content scheduled to run on any given day
    #     on the primary dashboard.
    #     """
    #
    #     from . import Item
    #
    #     #FIXME today, tomorrow if off by one day (hacky fix in place)
    #     # establish timeliness of content
    #     today = timezone.now().date() - timedelta(1)
    #     tomorrow = timezone.now().date()
    #     today_start = datetime.combine(today, time())
    #     today_end = datetime.combine(tomorrow, time())
    #
    #     # items where run_date=today
    #     running_today = Item.objects.filter(run_date__range=(today_start, today_end), organization=self)
    #
    #     return running_today

    # def get_org_stories_due_for_edit_today(self):
    #     """Return list of content scheduled for edit today.
    #
    #     Used to display content scheduled for edit on any given day
    #     on the primary dashboard.
    #     """
    #
    #     from .item import Item
    #
    #     #FIXME today, tomorrow if off by one day (hacky fix in place)
    #     # establish timeliness of content
    #     today = timezone.now().date() - timedelta(1)
    #     tomorrow = timezone.now().date()
    #     today_start = datetime.combine(today, time())
    #     today_end = datetime.combine(tomorrow, time())
    #
    #     edit_today = Item.objects.filter(due_edit__range=(today_start, today_end), organization=self)
    #
    #     return edit_today

    # def get_org_projects(self):
    #     """Return queryset of projects associated with a news organization for
    #     use in PlatformAccount forms.
    #     """
    #
    #     from . import Project
    #     projects = []
    #     networks = NewsOrganization.get_org_networks(self)
    #     network_projects = Project.objects.filter(share_with__in=networks)
    #     org_projects = Project.objects.filter(organization=self)
    #     projects.extend(network_projects)
    #     projects.extend(org_projects)
    #     return projects

    # def get_org_content_tasks(self):
    #     """Return all the tasks associated with projects, stories, or events.
    #
    #     This includes items from content that is collaborative.
    #     """
    #
    #     return self.task_set.all()

    # def get_org_events(self):
    #     """Return all the events associated with the org or org content.
    #
    #     This includes items from content that is collaborative.
    #     """
    #     return self.event_set.all()

    # def get_org_searchable_comments(self):
    #     """Return all the comments that should appear in search results.
    #
    #     This includes comments from items that are collaborative.
    #     """
    #     return self.get_org_participant_comments()

    # def get_org_searchable_notes(self):
    #     """Return all the notes that should appear in search results.
    #     This includes notes from items that are collaborative."""
    #
    #     return Note.objects.filter(participant__organization=self).exclude(note_type='Participant')

    # def get_org_searchable_content(self):
    #     """Return queryset of all objects that can be searched by a participant."""
    #
    #     from .projects import Project
    #     from .story import Story
    #     from .item import Item
    #
    #     #additional required info
    #     networks = self.get_org_networks()
    #
    #     searchable_objects = []
    #
    #     projects = Project.objects.filter(Q(Q(organization=self) | Q(partner_with=self)))
    #     stories = Story.objects.filter(Q(Q(organization=self) | Q(partner_with=self)))
    #     items = Item.objects.filter(Q(organization=self))
    #     imageassets = self.imageasset_set.all()
    #     documentassets = self.documentasset_set.all()
    #     audioassets = self.audioasset_set.all()
    #     tasks = self.get_org_content_tasks()
    #     events = self.get_org_events()
    #     comments = self.get_org_searchable_comments()
    #     notes = self.get_org_searchable_notes()
    #
    #     searchable_objects.append(projects)
    #     searchable_objects.append(stories)
    #     searchable_objects.append(items)
    #     searchable_objects.append(imageassets)
    #     searchable_objects.append(documentassets)
    #     searchable_objects.append(audioassets)
    #     searchable_objects.append(tasks)
    #     searchable_objects.append(events)
    #     searchable_objects.append(notes)
    #     searchable_objects.append(comments)
    #
    #     return searchable_objects

    # def get_org_itemtemplates(self):
    #     """Return queryset of item templates that should be available of org items."""
    #
    #     from . import ItemTemplate
    #
    #     return ItemTemplate.objects.filter(Q(organization_id__isnull=True) | Q(organization=self) & Q(is_active=True))


# @receiver(post_save, sender=NewsOrganization)
# def create_org_meta(sender, instance, created, **kwargs):
#     # Make a new NewsOrganization
#     if created:
#         # Create an EntityOwner record
#         instance.entity_owner_profile = EntityOwner.objects.create_entity_owner_record(
#             owner_type = 'NEWSORGANIZATION',
#             owner_name = instance.name,
#             owner_id = instance.id,
#         )
#         # Create a NetworkMember record
#         instance.network_member_profile = NetworkMember.objects.create_network_member_record(
#             member_type = 'NEWSORGANIZATION',
#             member_name = instance.name,
#             member_id = instance.id,
#         )
#         # Create an Anchor record
#         instance.anchor_profile = Anchor.objects.create_anchor_record(
#             anchor_type = 'NEWSORGANIZATION',
#             anchor_name = instance.name,
#             anchor_id = instance.id,
#         )
#         # Create Partner record
#         instance.partner_profile = Partner.objects.create_partner_record(
#             partner_type = 'NEWSORGANIZATION',
#             partner_name = instance.name,
#             partner_id = instance.id,
#         )
#         # Save Instance before adding Discussion
#         instance.save()
#         # Create Discussion, channel = 'main'
#         # Retrieve instance anchor_profile
#         main_discussion = Discussion.objects.create_discussion(
#             anchor=instance.anchor_profile,
#             channel='Main',
#         )
#         # Final Save
#         instance.save()

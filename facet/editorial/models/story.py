import time as timemk
from django.urls import reverse
from django.db import models
# from django.db.models import Q
# from django.shortcuts import get_object_or_404
from datetime import datetime
import time

from base.models import Participant, Anchor, EntityOwner, Partner
from note.models import Note
from .project import Project
#

class Story(models.Model):
    """The unit of a story.

    A story is the one or more items that make up a particular story.
    Sharing and collaboration is controlled at the story level.
    The story also controls the sensitivity and embargo status of the content.
    """

    anchor_profile = models.OneToOneField(Anchor, null=True, on_delete=models.SET_NULL)

    #ownership
    participant_owner = models.OneToOneField(
        Participant,
        help_text = 'Participant who created/owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that owns this.',
        blank=True,
        null = True,
        on_delete = models.SET_NULL,
    )

    project = models.ForeignKey(
        Project,
        blank=True,
        on_delete = models.SET_NULL,
        null=True,
    )

    # connection to participants participating in a story
    team = models.ManyToManyField(
        Participant,
        related_name='story_team_members',
        help_text='Contributing participant.',
        blank=True,
    )

    name = models.CharField(
        max_length=250,
        help_text='The name by which the story is identified.'
    )

    desc = models.TextField(
        blank=True,
        help_text='Short description of the story.'
    )


    original = models.BooleanField(
        default=True,
        help_text='If original to participant/entity, true. If picked up, false.',
        # If story is not original, set to false and use StoryPickupDetail for additional info.
    )

    embargo = models.BooleanField(
        default=False,
        help_text='Is a story embargoed?'
        )

    embargo_datetime = models.DateTimeField(
        help_text='When is the story no longer under embargo.',
        blank=True,
        null=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='When was the story created.'
    )

    sensitive = models.BooleanField(
        default=False,
        help_text='Is a story sensitive and viewing it limited only to the team working on it?'
    )

    share = models.BooleanField(
        default=False,
        help_text='The story is being shared with partners.'
    )

    share_date = models.DateTimeField(
        help_text="Estimated date the story will be available",
        blank=True,
        null=True,
    )

    ready_to_share = models.BooleanField(
        default=False,
        help_text='The story is finished and ready to be picked up.'
    )

    share_with = models.ManyToManyField(
        Partner,
        related_name='share_partners',
        help_text='Partner profiles selected to have access to shared content.',
        blank=True,
    )

    collaborate = models.BooleanField(
        default=False,
        help_text='The story is being collaborated on with partners.'
    )

    partner_with = models.ManyToManyField(
        Partner,
        related_name='story_collaboration_partners',
        help_text='Partner profiles selected to have collaborative access.',
        blank=True,
    )

    archived = models.BooleanField(
        default=False,
        help_text='Is the content no longer active and needed?'
    )


    # notes
    notes = models.ManyToManyField(Note, blank=True)
    # internal assets
    internal_image_assets = models.ManyToManyField('internalasset.InternalImage', blank=True)
    internal_document_assets = models.ManyToManyField('internalasset.InternalDocument', blank=True)
    internal_audio_assets = models.ManyToManyField('internalasset.InternalAudio', blank=True)
    internal_video_assets = models.ManyToManyField('internalasset.InternalVideo', blank=True)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = "Stories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('editorial:story_detail', kwargs={'pk': self.id})

    @property
    def description(self):
        return self.story_description

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Story"


    def get_team_vocab(self):
        """
        Team vocab should include:
        if story.project:
          use project.get_team_vocab()
        else:
          if partner_with:
              partipants from partner_profiles of actors or entities listed
          if entity_owner:
              staff_team of entity_owner
          if assignment.project = self:
              freelancer
          if story.guest:
              guest participant
          if participant_owner:
              participant_owner
        """

        partner_profiles = []
        vocab = []
        if self.project:
            # return project team
            vocab = Project.get_team_vocab(self.project)
        else:
            if self.partner_with:
              # retrieve partner profiles of participants and entities
              partners = self.partner_with.all()
              for entry in partners:
                  if entry.partner_type=='PARTICIPANT' or entry.partner_type=='NEWS ORGANIZATION':
                      partner_profiles.extend(entry)
                  if entry.partner_type=='NEWS ORGANIZATION NETWORK':
                      m_to_p = Network.convert_members_to_partners(entry)
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
                            m_to_p = Network.convert_members_to_partners(entry)
                            partner_profiles.extend(m_to_p)
                # if no entity_owner, participant_owner is team
                elif self.participant_owner and not entity_owner:
                    vocab.extend(self.participant_owner)

        # convert profiles to participants
        for entry in partner_profiles:
            if entry.partner_type=='PARTICIPANT':
                vocab.extend(entry.participant)
            else:
                team = NewsOrganization.get_staff_team(entry.newsorganization)
                vocab.extend(team_vocab)

        # Check for freelance assignment
        from freelance.models import Assignment
        assignment = Assignment.objects.filter(story=self)
        if assignment:
            vocab.extend(assignment.freelancer.participant)
        # Check for guests
        # TODO

        # Janky way of converting list back to a queryset so item form is happy
        # FIXME eventually
        team_vocab = Participant.objects.filter(id__in=vocab)

        return team_vocab

    # FIXME account for organization and participant filtering
    # def copy_story(self):
    #     """ Create a copy of a story for a partner organization in a network.
    #
    #     Copied stories keep all attributes.
    #
    #     Organization is set to the copier's organization and the original_content
    #     flag is set to false. Triggering a copy also triggers the creation of a
    #     story copy detail record.
    #     """
    #
    #     story_copy = get_object_or_404(Story, id=self.id)
    #
    #     # Set the id = None to create the copy the story instance
    #     story_copy.id = None
    #     story_copy.save()
    #
    #     # clear relationships if they exist
    #     if story_copy.share_with:
    #         story_copy.share_with.clear()
    #     if story_copy.partner_with:
    #         story_copy.partner_with.clear()
    #
    #     # clear attributes for the copying organization
    #     story_copy.original_story = False
    #     story_copy.sensitive = False
    #     story_copy.share = False
    #     story_copy.ready_to_share = False
    #     story_copy.collaborate = False
    #     story_copy.archived = False
    #     story_copy.discussion = Discussion.objects.create_discussion("STO")
    #     story_copy.save()
    #
    #     return story_copy

    # def get_story_download(self):
    #     """Return rst formatted string for downloading story meta."""
    #
    #     # loop over m2m and get the values as string
    #     team = self.team.all()
    #     team = [participant.credit_name for participant in team]
    #     team = ",".join(team)
    #
    #     share_with = self.share_with.all()
    #     share_with = [org.name for org in share_with]
    #     share_with = ",".join(share_with)
    #
    #     partner_with = self.share_with.all()
    #     partner_with = [org.name for org in partner_with]
    #     partner_with = ",".join(partner_with)
    #
    #     # verify the text area fields have correct encoding
    #     name = self.name.encode('utf-8')
    #     # print "NAME: ", name
    #     description = self.story_description.encode('utf-8')
    #
    #     story_download = """
    #     Story\r\n
    #     ========\r\n
    #     {name}\r\n
    #     --------------\r\n
    #     Description: {desc}\r\n
    #     Owner: {owner}\r\n
    #     Organization: {organization}\r\n
    #     Original: {original}\r\n
    #     Team: {team}\r\n
    #     Created: {created}\r\n
    #     Sensitive: {sensitive}\r\n
    #     Embargo Status: {embargo}\r\n
    #     Embargo Date/Time: {embargo_dt}\r\n
    #     Share: {share}\r\n
    #     Share Date: {sharedate}\r\n
    #     Shared With: {sharewith}\r\n
    #     Ready for Sharing: {shareready}\r\n
    #     Collaborate: {collaborate}\r\n
    #     Collaborate With: {collaboratewith}\r\n
    #     Archived: {archived}\r\n
    #     """.format(name=name, desc=description, owner=self.owner, organization=self.organization.name,
    #     original=self.original_story, team=team, created=self.creation_date, sensitive=self.sensitive,
    #     embargo=self.embargo, embargo_dt=self.embargo_datetime, share=self.share,
    #     sharedate=self.share_with_date, sharewith=share_with, shareready=self.ready_to_share,
    #     collaborate=self.collaborate, collaboratewith=partner_with, archived=self.archived)
    #     return story_download

    # # formerly get_story_team
    # def get_story_team_vocab(self):
    #     """Return queryset with org participants and participants from collaboration orgs for a story.
    #     Used in selecting credit and editors for a item.
    #     """
    #
    #     from . import Participant
    #     # TODO future: add contractors added to a story
    #     collaborators = self.partner_with.all()
    #     story_team = Participant.objects.filter(Q(Q(organization=self.organization) | Q(organization__in=collaborators)))
    #     return story_team

    # def get_story_images(self):
    #     """Return all the images associated with a story."""
    #
    #     story_images = []
    #     for item in self.item_set.all():
    #         images = item.get_item_images()
    #         story_images.extend(images)
    #     return story_images

    # def get_story_documents(self):
    #     """Return all documents associated with a story."""
    #
    #     story_documents = []
    #     for item in self.item_set.all():
    #         documents = item.get_item_documents()
    #         story_documents.extend(documents)
    #     return story_documents

    # def get_story_audio(self):
    #     """Return all audio associated with a story."""
    #
    #     story_audio = []
    #     for item in self.item_set.all():
    #         audio = item.get_item_audio()
    #         story_audio.extend(audio)
    #     return story_audio

    # def get_story_video(self):
    #     """ Return all video associated with a story."""
    #
    #     story_video = []
    #     for item in self.item_set.all():
    #         video = item.get_item_video()
    #         story_video.extend(video)
    #     return story_video

    # def get_story_items(self):
    #     """Return all existing items associated with a story."""
    #
    #     return self.item_set.all()
    #
    #     # {% for item in story.get_story_items %}
    #     #    <a href="{{ item.get_absolute_url }}">{{ item.name }}</a>
    #     # {% endfor %}

    # def get_story_items_schedule(self):
    #     """Return deadlines of a story and its items.
    #     Used for inclusion with project schedules.
    #
    #     Includes:
    #     story_share_date
    #     item due_edit
    #     item run_date
    #     """
    #
    #     data = []
    #
    #     story = Story.objects.get(pk=self.id)
    #
    #     # gather story dates for stories to be shared
    #     if story.share_with_date:
    #         shared_story_dict = {}
    #
    #         item_date = story.share_with_date
    #
    #         shared_story_dict['id'] = story.id
    #         shared_story_dict['title'] = story.name
    #         shared_story_dict['share_with_date'] = item_date.isoformat()
    #         shared_story_dict['url'] = story.get_absolute_url()
    #         shared_story_dict['start'] = item_date.isoformat()
    #         shared_story_dict['end'] = item_date.isoformat()
    #         shared_story_dict['overlap'] = True
    #         shared_story_dict['all_day'] = False
    #         shared_story_dict['backgroundColor'] = '#F44336'
    #         shared_story_dict['textColor'] = 'fff'
    #         shared_story_dict['class'] = "calevent"
    #
    #         data.append(shared_story_dict)
    #
    #     # gather schedule dates for all story items
    #     if story.item_set.all():
    #         for item in story.item_set.all():
    #             if item.due_edit:
    #                 item_edit_dict = {}
    #
    #                 item_date = item.due_edit
    #
    #                 item_edit_dict['id'] = item.id
    #                 item_edit_dict['title'] = item.name
    #                 item_edit_dict['due_edit'] = item_date.isoformat()
    #                 item_edit_dict['url'] = item.get_absolute_url()
    #                 item_edit_dict['start'] = item_date.isoformat()
    #                 item_edit_dict['end'] = item_date.isoformat()
    #                 item_edit_dict['overlap'] = True
    #                 item_edit_dict['all_day'] = False
    #                 item_edit_dict['backgroundColor'] = '#FFA000'
    #                 item_edit_dict['textColor'] = 'fff'
    #                 item_edit_dict['class'] = "calevent"
    #
    #                 data.append(item_edit_dict)
    #
    #             if item.run_date:
    #                 item_run_dict = {}
    #
    #                 item_date = item.run_date
    #
    #                 item_run_dict['id'] = item.id
    #                 item_run_dict['title'] = item.name
    #                 item_run_dict['run_date'] = item_date.isoformat()
    #                 item_run_dict['url'] = item.get_absolute_url()
    #                 item_run_dict['start'] = item_date.isoformat()
    #                 item_run_dict['end'] = item_date.isoformat()
    #                 item_run_dict['overlap'] = True
    #                 item_run_dict['all_day'] = False
    #                 item_run_dict['backgroundColor'] = '#7CB342'
    #                 item_run_dict['textColor'] = 'fff'
    #                 item_run_dict['class'] = "calevent"
    #
    #                 data.append(item_run_dict)
    #
    #     return data
    #
    # def get_story_event_schedule(self):
    #     """Return story events for a story.
    #
    #     Used for returning a single story's event schedule.
    #     """
    #
    #     data = []
    #
    #     story = Story.objects.get(pk=self.id)
    #
    #     # gather schedule dates for all story events
    #     if story.event_set.all():
    #         for event in story.event_set.filter(event_type="Hosting"):
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
    #         for event in story.event_set.filter(event_type="Reporting"):
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
    #         for event in story.event_set.filter(event_type="Administrative"):
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
    #         for event in story.event_set.filter(event_type="Other"):
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
    #
    # def get_story_schedule(self):
    #     """Return all the relevant dates for a story.
    #     Used for returning a single story's schedule.
    #
    #     Includes:
    #     story_share_date
    #     item due_edit
    #     item run_date
    #     event event_date
    #     task due_date
    #     """
    #
    #     data = []
    #
    #     story = Story.objects.get(pk=self.id)
    #
    #     # gather story dates for stories to be shared
    #     if story.share_with_date:
    #         shared_story_dict = {}
    #
    #         item_date = story.share_with_date
    #
    #         shared_story_dict['id'] = story.id
    #         shared_story_dict['title'] = story.name
    #         shared_story_dict['share_with_date'] = item_date.isoformat()
    #         shared_story_dict['url'] = story.get_absolute_url()
    #         shared_story_dict['start'] = item_date.isoformat()
    #         shared_story_dict['end'] = item_date.isoformat()
    #         shared_story_dict['overlap'] = True
    #         shared_story_dict['all_day'] = False
    #         shared_story_dict['backgroundColor'] = '#F44336'
    #         shared_story_dict['textColor'] = 'fff'
    #         shared_story_dict['class'] = "calevent"
    #
    #         data.append(shared_story_dict)
    #
    #     # gather schedule dates for all story items
    #     if story.item_set.all():
    #         for item in story.item_set.all():
    #             if item.due_edit:
    #                 item_edit_dict = {}
    #
    #                 item_date = item.due_edit
    #
    #                 item_edit_dict['id'] = item.id
    #                 item_edit_dict['title'] = item.name
    #                 item_edit_dict['due_edit'] = item_date.isoformat()
    #                 item_edit_dict['url'] = item.get_absolute_url()
    #                 item_edit_dict['start'] = item_date.isoformat()
    #                 item_edit_dict['end'] = item_date.isoformat()
    #                 item_edit_dict['overlap'] = True
    #                 item_edit_dict['all_day'] = False
    #                 item_edit_dict['backgroundColor'] = '#FFA000'
    #                 item_edit_dict['textColor'] = 'fff'
    #                 item_edit_dict['class'] = "calevent"
    #
    #                 data.append(item_edit_dict)
    #
    #             if item.run_date:
    #                 item_run_dict = {}
    #
    #                 item_date = item.run_date
    #
    #                 item_run_dict['id'] = item.id
    #                 item_run_dict['title'] = item.name
    #                 item_run_dict['run_date'] = item_date.isoformat()
    #                 item_run_dict['url'] = item.get_absolute_url()
    #                 item_run_dict['start'] = item_date.isoformat()
    #                 item_run_dict['end'] = item_date.isoformat()
    #                 item_run_dict['overlap'] = True
    #                 item_run_dict['all_day'] = False
    #                 item_run_dict['backgroundColor'] = '#7CB342'
    #                 item_run_dict['textColor'] = 'fff'
    #                 item_run_dict['class'] = "calevent"
    #
    #                 data.append(item_run_dict)
    #
    #     # gather schedule dates for all story events
    #     if story.event_set.all():
    #         for event in story.event_set.filter(event_type="Hosting"):
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
    #         for event in story.event_set.filter(event_type="Reporting"):
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
    #         for event in story.event_set.filter(event_type="Administrative"):
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
    #         for event in story.event_set.filter(event_type="Other"):
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
    #     if story.task_set.all():
    #         for task in story.task_set.all():
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
    #
    # def get_story_events(self):
    #     """Return all story events."""
    #
    #     return self.event_set.all()



    # def is_editable_by_org(self, org):
    #     """Can this story be edited by this org?"""
    #
    #     # FIXME: add contractor access?
    #
    #     return (org == self.organization or
    #          (self.collaborate and org in self.partner_with.all()))

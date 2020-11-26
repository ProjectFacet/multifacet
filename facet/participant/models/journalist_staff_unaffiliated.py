from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from entity.models import NewsOrganization
from base.models import Participant
from participant.models import StaffJournalist

class UnaffiliatedStaffJournalist(models.Model):
    """ A Staff Journalist whose organization is not on platform.
    """

    participant = models.OneToOneField(
        Participant,
        on_delete=models.CASCADE,
    )

    # If converted to staff journalist, maintain connection
    staffjournalist = models.ForeignKey(
        StaffJournalist,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text = 'Account of Affiliated Staff Journalist',
    )

    # Collect name of news organization for later possible affiliation
    newsorganization = models.CharField(
        max_length=350,
        blank=True,
        help_text='Name of the off platform news organization.',
    )

    newsorganization_website = models.URLField(
        max_length=500,
        help_text='Link to news organization website.',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Unaffiliated Staff Journalist'
        verbose_name_plural = 'Unaffiliated Staff Journalists'


    def __str__(self):
        return self.participant.credit_name

    # def get_absolute_url(self):
    #     return reverse('staffjournalist_detail', kwargs={'pk': self.id})

    @property
    def description(self):
        org = self.newsorganization

        return "{staff_journalist}, {title}, {org} (Organization Not on Platform)".format(
                                        staff_journalist=self.participant.credit_name,
                                        title=self.participant.title,
                                        org=org,
                                        )

    @property
    def search_title(self):
        return self.credit_name

    @property
    def type(self):
        return 'Unaffiliated Staff Journalist'


    def get_projects(self):
        """Return list of all project an unaffiliated staff journalist is associated with."""

        participant = self.participant
        projects_owner = participant.participant_owner.all()
        projects_team = participant.project_team_member.all()
        unaffiliatedstaff_journalist_projects = []
        unaffiliatedstaff_journalist_projects.extend(projects_owner)
        unaffiliatedstaff_journalist_projects.extend(projects_team)
        return unaffiliatedstaff_journalist_projects


    def get_itemtemplates(self):
        """Return queryset of item templates that should be available."""

        from editorial.models import ItemTemplate

        return ItemTemplate.objects.filter(Q(sitewide=True) | Q(participant_owner=self.participant) & Q(is_active=True))


    # def get_staffjournalist_content(self):
    #     """Return list of all content staff journalist is associated with as
    #     owner, editor or credit.
    #
    #     Results are used to display relevant content for a staff journalist on
    #     their dashboard and staff journalist profile.
    #     """
    #
    #     staffjournalist_content = []
    #     projects_owner = self.project_owner.all()
    #     projects_team = self.project_team_member.all()
    #     story_owner = self.story_owner.all()
    #     story_team = self.story_team_member.all()
    #     item_owner = self.item_owner.all()
    #     # item_team = self.team.all()
    #     staffjournalist_content.extend(projects_owner)
    #     staffjournalist_content.extend(projects_team)
    #     staffjournalist_content.extend(story_owner)
    #     staffjournalist_content.extend(story_team)
    #     staffjournalist_content.extend(item_owner)
    #
    #     return staffjournalist_content
    #
    # def get_staffjournalist_assets(self):
    #     """Return assets that a staff journalist is associated with."""
    #
    #     staffjournalist_assets = []
    #     images_owner = self.imageasset_set.all()
    #     documents_owner = self.documentasset_set.all()
    #     audio_owner = self.audioasset_set.all()
    #     video_owner = self.videoasset_set.all()
    #     staffjournalist_assets.extend(images_owner)
    #     staffjournalist_assets.extend(documents_owner)
    #     staffjournalist_assets.extend(audio_owner)
    #     staffjournalist_assets.extend(video_owner)
    #
    #     return staffjournalist_assets
    #
    # def get_staffjournalist_tasks(self):
    #     """Return all the tasks for a staff journalist."""
    #
    #     from . import Task
    #
    #     tasks = Task.objects.filter(Q(owner=self) | Q(assigned_to=self))
    #     return tasks

    # def inbox_comments(self):
    #     """Return list of comments from discussions the staff journalist is a participant in.
    #
    #     Collects all relevant comments for a specific staff journalist to show in their
    #     dashboard and inbox.
    #     """
    #
    #     from . import Comment
    #
    #     staffjournalist_discussion_ids = self.comment_set.all().values('discussion_id')
    #
    #     return (Comment
    #             .objects
    #             .filter(discussion_id__in=staffjournalist_discussion_ids)
    #             .exclude(staffjournalist_id=self.id)
    #             .select_related('participant', 'discussion')
    #             )

    # def recent_comments(self):
    #     """Recent comments in staff journalists's discussions.
    #
    #     Return list of comments:
    #      - from discussions the staff journalist is a participant in
    #      - since the staff journalist's last login
    #      - where the staff journalist isn't the author
    #
    #     For display on primary dashboard.
    #     """
    #
    #     # FIXME: this appear to just be a subset of inbox_comments; can this use that?
    #
    #     from . import Comment
    #
    #     # Discussions staff journalist is involved in
    #     staffjournalist_discussion_ids = self.comment_set.all().values('discussion_id')
    #
    #     # Comments tht
    #     return (Comment
    #             .objects
    #             .filter(discussion_id__in=staffjournalist_discussion_ids,
    #                     date__gte=self.last_login)
    #             .exclude(staffjournalist_id=self.id)
    #            )

    # formerly get_staffjournalist_contact_list
    # def get_staffjournalist_contact_list_vocab(self):
    #     """ Return queryset containing all staff journalists a specific staff journalist can contact.
    #     This includes any staff journalist that's a member of an organization in network.
    #
    #     This vocab list populates to selection for messaging.
    #     """
    #
    #     organization = self.organization
    #     org_collaborators = organization.get_org_collaborators_vocab()
    #     contact_list = StaffJournalist.objects.filter(Q(Q(organization__in=org_collaborators) | Q(organization=organization)))
    #     return contact_list
    #
    # def private_messages_received(self):
    #     """ Return all private messages a staff journalist is a recipient of.
    #
    #     Displayed in staff journalist inbox under 'inbox'.
    #     """
    #     return self.private_message_recipient.all()
    #
    # def private_messages_sent(self):
    #     """ Return all private messages a staff journalist has sent.
    #
    #     Displayed in staff journalist inbox under 'sent'.
    #     """
    #     return self.private_message_sender.all()
    #
    # def get_staffjournalist_searchable_content(self):
    #     """ Return queryset of staff journalist specific content that is searchable.
    #
    #     A staff journalist can return their own notes in search results.
    #     """
    #     return self.participantnote_owner.all()

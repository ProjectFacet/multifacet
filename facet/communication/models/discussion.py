"""
Discussions can be associated with:
NewsOrganization
NewsOrganizationNetwork
Project
Story
Item
Task
Event
Pitch
Assignment

The relationship is One to Many

Ex: One NewsOrganization can have multiple discussions with unique channels

The relationship is managed throught contenttypes to allow for multiple kinds of
anchor objects.

A generic foreign key manages the backward relationship.

Access: Any participant with access to the ownership object can participate in
a Discussion, seeing and contributing comments.

"""

from django.db import models

from base.models import Anchor


class DiscussionManager(models.Manager):
    """ Custom manager for discussions."""

    def create_discussion(self, discussion_type, anchor, channel):
        """ Method for quick creation of a discussion."""
        discussion = self.create(anchor=anchor, channel=channel)
        return discussion


class Discussion(models.Model):
    """ Container class for Comments.

    Standard value for channel is 'main' for models that only
    get one channel: Story, Item, Task, Event, Pitch, Assignment.

    The anchor connects the discussion to another object:
    Organization, Network, Project, Story, Item,
    Task, Event, Pitch, Assignment.
    """

    channel = models.CharField(
        max_length=250,
        help_text='Name of specific discussion.',
    )

    anchor = models.OneToOneField(
        Anchor,
        on_delete=models.CASCADE,
        help_text='The anchor object',
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ['channel', 'anchor']
        ordering = ['-creation_date']

    objects = DiscussionManager()

    def __str__(self):
        return "{anchor} {discussion_type} Discussion: {channel}".format(
            anchor = content_object,
            discussion_type=self.discussion_type,
            channel = channel,
        )

from django.db import models

class AnchorManager(models.Manager):
    """Custom manager for Anchor."""

    def create_anchor_record(self, anchor_type, anchor_name, anchor_id):
        """Method that takes in type, name and id for quick access."""

        anchor = self.create(anchor_type=anchor_type, anchor_name=anchor_name, anchor_id=anchor_id)
        return anchor


class Anchor(models.Model):
    """Connection between different anchors that objects can be connected to.

    Models that can be anchors:
    _Organization, _Network, Project, Story, Item, Task, Event +
    Pitch, Assignment

    Models that can be anchored:
    Task, Event, Note, Discussion +

    Models that are anchors point at an Anchor record as the
    anchor_profile

    Anchored models point to Anchor records as the anchor.

    Ex. A Project has an Anchor record and a Project have many tasks.
    A task has a field anchor that points to that Anchor record. Multiple tasks
    can point anchor record.

    This allows for consistency across multiple kinds of Anchors.

    Additional internal information is included on the record for easy access.
    """

    # Choices for Anchor Type
    NEWSORGANIZATION = 'NEWS ORGANIZATION'
    NEWSORGANIZATIONNETWORK = 'NEWS ORGANIZATION NETWORK'
    PROJECT = 'PROJECT'
    STORY = 'STORY'
    ITEM = 'ITEM'
    TASK = 'TASK'
    EVENT = 'EVENT'
    PITCH = 'PITCH'
    ASSIGNMENT = 'ASSIGNMENT'

    ANCHOR_TYPE_CHOICES = (
        (NEWSORGANIZATION, 'News Organization'),
        (NEWSORGANIZATIONNETWORK, 'News Organization Network'),
        (PROJECT, 'Project'),
        (STORY, 'Story'),
        (ITEM, 'Item'),
        (TASK, 'Task'),
        (EVENT,'Event'),
        (PITCH, 'Pitch'),
        (ASSIGNMENT, 'Assignment'),
    )

    anchor_type = models.CharField(
        max_length=250,
        choices=ANCHOR_TYPE_CHOICES,
        help_text='What kind of anchor it is.'
    )

    anchor_name = models.CharField(
        max_length=250,
        help_text='Name of the anchor.',
    )

    anchor_id = models.PositiveIntegerField()

    objects = AnchorManager()

    class Meta:
        verbose_name = 'Anchor Profile'
        verbose_name_plural = "Anchor Profiles"

    def __str__(self):
        return self.anchor_name

    @property
    def description(self):
        return "Anchor Profile for {anchor_type} {anchor_name} ({anchor_id})".format(
            anchor_type=self.anchor_type,
            anchor_name=self.anchor_name,
            anchor_id=self.anchor_id,
        )

    @property
    def type(self):
        return "Anchor Profile"


    def get_absolute_url(self):
        """Get get_absolute_url of actual object."""

        if self.newsorganization:
            return self.newsorganization.get_absolute_url()
        if self.newsorganizationnetwork:
            return self.newsorganizationnetwork.get_absolute_url()
        if self.project:
            return self.project.get_absolute_url()
        if self.story:
            return self.story.get_absolute_url()
        if self.item:
            return self.item.get_absolute_url()
        if self.task:
            return self.task.get_absolute_url()
        if self.event:
            return self.event.get_absolute_url()
        if self.pitch:
            return self.pitch.get_absolute_url()
        if self.assignment:
            return self.assignment.get_absolute_url()

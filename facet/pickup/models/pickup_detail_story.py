from django.db import models

from base.models import Participant, Partner, EntityOwner
from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset

class StoryPickupDetailManager(models.Manager):
    """Custom manager to create pickup records for stories. """

    def create_story_pickup_record(self, original_entity_owner, partner, original_story, partner_story):
        """Method for quick creation of a pickup record."""
        story_pickup_detail=self.create(original_entity_owner=original_entity_owner, partner=partner, original_story=original_story, partner_story=partner_story)
        return story_pickup_detail


class StoryPickupDetail(models.Model):
    """ The details of each pickup of a story.

    Each time an organization elects to pickup a shared facet, query to see if the
    story has already been copied over. If not, pickup the story to the new organization.
    """

    original_entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that originally made the story available.',
    )

    original_story = models.ForeignKey(
        Story,
        help_text='ID of original instance of the story.',
        related_name='original_story_detail',
    )

    partner = models.ManyToManyField(
        Partner,
        related_name='story_pickup_partner',
        help_text='Partner picking up the story.',
        blank=True,
    )

    partner_story = models.ForeignKey(
        Story,
        help_text='ID of the new instance of the story saved by the pickup partner.',
        related_name='story_pickup',
    )

    pickup_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Datetime when pickup was made.'
    )

    objects = StoryPickupDetailManager()

    def __str__(self):
        return "Copyinfo for {pickup_partner} \'s pickup of story: {story}".format(
                                pickup_partner=self.partner.partner_name,
                                story=self.original_story,
                                )

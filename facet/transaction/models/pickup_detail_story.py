# from django.db import models
#
# from editorial.models import Story, Item, DocumentAsset, ImageAsset, AudioAsset, VideoAsset
# from entity.models import NewsOrganization
# from base.models import Participant
#
# class StoryPickupDetailManager(models.Manager):
#     """Custom manager to create pickup records for stories. """
#
#     def create_story_pickup_record(self, original_org, partner, original_story, partner_story):
#         """Method for quick creation of a pickup record."""
#         story_pickup_detail=self.create(original_org=original_org, partner=partner, original_story=original_story, partner_story=partner_story)
#         return story_pickup_detail
#
#
# @python_2_unicode_compatible
# class StoryPickupDetail(models.Model):
#     """ The details of each pickup of a story.
#
#     Each time an organization elects to pickup a shared facet, query to see if the
#     story has already been copied over. If not, pickup the story to the new organization.
#     """
#
#     original_org = models.ForeignKey(
#         NewsOrganization,
#         help_text='News Organizationthat originally created the content.',
#         related_name='original_story_organization',
#     )
#
#     original_story = models.ForeignKey(
#         Story,
#         help_text='Original instance of the story.',
#         related_name='original_story_detail',
#     )
#
#     partner = models.ForeignKey(
#         NewsOrganization,
#         help_text='News Organization that is picking up the story.',
#         related_name='pickup_organization',
#     )
#
#     partner_story = models.ForeignKey(
#         Story,
#         help_text='The new instance of the story saved by the partner organization.',
#         related_name='story_pickup',
#     )
#
#     pickup_date = models.DateTimeField(
#         auto_now_add=True,
#         help_text='Datetime when pickup was made.'
#     )
#
#     objects = StoryPickupDetailManager()
#
#     def __str__(self):
#         return "Copyinfo for {pickuporg} \'s pickup of story: {story}".format(
#                                 pickuporg=self.partner.name,
#                                 story=self.original_story,
#                                 )

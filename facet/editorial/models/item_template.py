# from django.contrib.postgres.fields import ArrayField
# # from django.core.urlresolvers import reverse
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# # from simple_history.models import HistoricalRecords
#
# # from base.models import Participant
# # from entity.NewsOrganization import NewsOrganization
#
#
# #-----------------------------------------------------------------------#
# #   ITEM
# #-----------------------------------------------------------------------#
#
# class ItemTemplate(models.Model):
#     """Template for items.
#
#     A template is a collection of fields so that when adding/editing an item,
#     only appropriate fields are shown.
#     """
#
#     # owner = models.ForeignKey(
#     #     'Participant',
#     #     blank=True,
#     #     null=True,
#     # )
#
#     # A template without an entity owner is a "site-wide" template;
#     # when listing templates for an organization, list the site-wide and
#     # ones that match the organization.
#     content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     sitewide = models.BooleanField(
#         help_text = 'If no ownership entity, True.',
#         default=False,
#     )
#
#     name = models.CharField(
#         max_length=50,
#     )
#
#     description = models.CharField(
#         max_length=100,
#         blank=True,
#     )
#
#     fields_used = ArrayField(
#         models.CharField(max_length=50),
#         default=list,
#         help_text='Fields used by this template.',
#         blank=True,
#     )
#
#     creation_date = models.DateTimeField(
#         auto_now_add=True,
#         help_text='When template was created.',
#         blank=True,
#     )
#
#     is_active = models.BooleanField(
#         default=True,
#     )
#
#     class Meta:
#         ordering = ['id']
#         unique_together = ['name', 'content_object']
#
#     def __str__(self):
#         return self.name
#
#     @property
#     def search_title(self):
#         return self.name
#
#     @property
#     def type(self):
#         return "Item Template"
#
#     # def get_absolute_url(self):
#     #     if self.content_object:
#     #         return reverse('item_template_edit', kwargs={'template': self.id, 'org': self.content_object.id })
#     #     else:
#     #         return reverse('item_template_detail', kwargs={'template': self.id})
#
#     # def copy(self):
#     #     """ Create a copy of an item template for a partner organization in a network."""
#     #
#     #     print("in item template copy")
#     #     self.id = None
#     #     self.is_active=False
#     #     print("pre copy save")
#     #     self.save()
#     #     print("saved")
#     #     print("new id", self.id)
#     #     return self
#
# # field which will appear on all item-editing forms -- and therefore do not
# # need to be in the "fields_used" for a template.
#
# COMMON_FIELDS = {
#     "name",
#     "headline",
#     "description",
#     "editor",
#     "credit",
#     # "team",
#     "content",
#     "status",
#     "due_edit",
#     "run_date",
#     # "template",
#     # "story",
# }

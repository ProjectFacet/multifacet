# """
# Discussions can be associated with:
# NewsOrganization
# NewsOrganizationNetwork
# Project
# Story
# Item
# Task
# Event
# Pitch
# Assignment
#
# The relationship is One to Many
#
# Ex: One NewsOrganization can have multiple discussions with unique channels
#
# The relationship is managed throught contenttypes to allow for multiple kinds of
# anchor objects.
#
# A generic foreign key manages the backward relationship.
#
# Access: Any participant with access to the ownership object can participate in
# a Discussion, seeing and contributing comments.
#
# """
#
# from django.db import models
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
#
# # from base.models import Participant
# # from entity.models import NewsOrganization, NewsOrganizationNetwork
# # from editorial.models import Project, Story, Item
# # from task.models import Task
# # from note.models import Note
# # from event.models import Event
# # from freelance.models import Pitch, Assignment
#
# class DiscussionManager(models.Manager):
#     """ Custom manager for discussions."""
#
#     def create_discussion(self, discussion_type):
#         """ Method for quick creation of a discussion."""
#         discussion = self.create(discussion_type=discussion_type, content_object=anchor, channel=channel)
#         return discussion
#
#
# @python_2_unicode_compatible
# class Discussion(models.Model):
#     """ Container class for Comments."""
#
#     # default value is 'main'
#     # for story, item, task, event, pitch, assignment only have one channel
#     channel = models.CharField(
#         max_length=250
#         help_text='Name of specific discussion.'
#     )
#
#     # Relation to anchor object:
#     # Organization, Network, Project, Story, Item
#     # Task, Event, Pitch, Assignment
#     # On the anchor model:
#     # discussion = GenericRelation(Discussion)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     # On the anchor model:
#     # discussion = GenericRelation(Discussion)
#
#     # Choices for Discussion type
#     ORGANIZATION = 'ORGANIZATION'
#     NETWORK = 'NETWORK'
#     DIRECT = 'DIRECT'
#     PROJECT = 'PROJECT'
#     STORY = 'STORY'
#     ITEM = 'ITEM'
#     TASK = 'TASK'
#     EVENT = 'EVENT'
#     PITCH = 'PITCH'
#     ASSIGNMENT = 'ASSIGNMENT'
#
#     DISCUSSION_TYPE_CHOICES = (
#         (ORGANIZATION, 'Organization Discussion'),
#         (NETWORK, 'Network Discussion'),
#         (DIRECT, 'Direct Discussion'),
#         (PROJECT, 'Project Discussion'),
#         (STORY, 'Story Discussion'),
#         (ITEM, 'Item Discussion'),
#         (TASK, 'Task Discussion'),
#         (EVENT, 'Event Discussion'),
#         (PITCH, 'Pitch Discussion'),
#         (ASSIGNMENT, 'Assignment Discussion'),
#     )
#
#     discussion_type = models.CharField(
#         max_length=25,
#         choices=DISCUSSION_TYPE_CHOICES,
#         help_text='What kind of discussion it is.'
#     )
#
#     creation_date = models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     class Meta:
#         unique_together = ['channel', 'content_object']
#         ordering = ['-creation_date']
#
#     objects = DiscussionManager()
#
#     def __str__(self):
#         return "{anchor} {discussion_type} Discussion: {channel}".format(
#             anchor = content_object,
#             discussion_type=self.discussion_type,
#             channel = channel,
#         )

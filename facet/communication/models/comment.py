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
#
# class CommentManager(models.Manager):
#     """ Custom manager for comments."""
#
#     def create_comment(self, user, discussion, text):
#         """ Method for quick creation of a discussion."""
#         comment = self.create(user=user, discussion=discussion, text=text)
#         return comment
#
#
# class Comment(models.Model):
#     """An individual comment.
#
#     Comments can be made on a storyplan, facet,
#     or between one or more people privately.
#     """
#
#     user = models.ForeignKey(
#         User,
#     )
#
#     discussion = models.ForeignKey(
#         Discussion,
#     )
#
#     text = models.TextField(
#         help_text='The content of the comment.'
#     )
#
#     date = models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     objects = CommentManager()
#
#     class Meta:
#         ordering = ['-date']
#
#     def __str__(self):
#         return "Comment:{comment} from {discussion_type} discussion:{discussion} ({date})".format(
#                                 comment=self.id,
#                                 discussion=self.discussion.id,
#                                 discussion_type=self.discussion.discussion_type,
#                                 date=date,
#                                 )
#
#     @property
#     def type(self):
#         return "Comment"
#
#
# # class CommentReadStatus(models.Model):
# #     """ Tracking if a user involved in a discussion has read the most recent
# #     comment in order to surface unread comments first.
# #     """
# #
# #     comment = models.ForeignKey(
# #         Comment,
# #     )
# #
# #     user = models.ForeignKey(
# #         User,
# #     )
# #
# #     datetime_read = models.DateTimeField(
# #         auto_now_add=True,
# #     )
# #
# #     has_read = models.BooleanField(
# #         default=True,
# #     )
# #
# #     def __str__(self):
# #         return "Comment:{comment} has {status} read status.".format(
# #                                 comment=self.comment.id,
# #                                 status=self.has_read,
# #                                 )

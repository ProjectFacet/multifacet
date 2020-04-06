from django.db import models

from base.models import Participant
from .discussion import Discussion


class CommentManager(models.Manager):
    """ Custom manager for comments."""

    def create_comment(self, participant, discussion, text):
        """ Method for quick creation of a discussion."""
        comment = self.create(participant=participant, discussion=discussion, text=text)
        return comment


class Comment(models.Model):
    """An individual comment.

    Comments can be made on any discussion.
    """

    participant = models.ForeignKey(
        Participant,
        on_delete = models.CASCADE,
    )

    discussion = models.ForeignKey(
        Discussion,
        on_delete = models.CASCADE,
    )

    text = models.TextField(
        help_text='The content of the comment.'
    )

    date = models.DateTimeField(
        auto_now_add=True,
    )

    objects = CommentManager()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "Comment:{comment} from {discussion_type} discussion:{discussion} ({date})".format(
                                comment=self.id,
                                discussion=self.discussion.id,
                                discussion_type=self.discussion.discussion_type,
                                date=date,
                                )

    @property
    def type(self):
        return "Comment"


# class CommentReadStatus(models.Model):
#     """ Tracking if a participant involved in a discussion has read the most recent
#     comment in order to surface unread comments first.
#     """
#
#     comment = models.ForeignKey(
#         Comment,
#     )
#
#     participant = models.ForeignKey(
#         Participant,
#     )
#
#     datetime_read = models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     has_read = models.BooleanField(
#         default=True,
#     )
#
#     def __str__(self):
#         return "Comment:{comment} has {status} read status.".format(
#                                 comment=self.comment.id,
#                                 status=self.has_read,
#                                 )

from django.db import models

from base.models import Participant
from .directmessage_exchange import DirectMessageExchange


class DirectMessageManager(models.Manager):
    """ Customer manager for direct messaging."""

    def create_direct_message(self, message, text):
        """Method for quick creation of a direct message."""

        message = self.create(author=author, exchange=exchange, text=text)
        return message


class DirectMessage(models.Manager):
    """Messages in a direct message exhange."""

    # FIXME Should message delete if a participant is deleted?
    author = models.ForeignKey(
        Participant,
        help_text = 'Participant who authored the message.',
        on_delete = models.CASCADE,
    )

    exchange = models.ForeignKey(
        DirectMessageExchange,
        help_text = 'The exchange of participants this message is meant for.',
        on_delete = models.CASCADE,
    )

    text = models.TextField(
        help_text='The content of the message.'
    )

    date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time for creation of message.'
    )

    read = models.BooleanField(
        help_text = 'Has the message been seen by all participants.',
        default=False,
    )

    objects = DirectMessageManager()

    class Meta:
        verbose_name = 'Direct Message'
        verbose_name_plural = "Direct Messages"
        ordering = ['-date']

    def __str__(self):

        return "{author} message to { exchange } ({date})".format(
            author=author,
            exchange=exchange,
            date=date,
        )

    @property
    def type(self):
        return "Direct Message"

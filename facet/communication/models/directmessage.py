from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from base.models import Participant, Anchor
from entity.models import NewsOrganization, NewsOrganizationNetwork
from editorial.models import Project, Story, Item
from task.models import Task
from note.models import Note
from event.models import Event
from freelance.models import Pitch, Assignment

class DirectMessageExchangeManager(models.Manager):
    """ Customer manager for direct messaging."""

    def create_direct_message_exchange(self, participants):
        """Method for quick creation of a direct message."""

        exchange = self.create(participants=participants)
        return message


class DirectMessageExchange(models.Model):
    """ Direct message conversations can occur between two or more individuals and only exist in their
    own inboxes and are not attached to any other objects.

    Different from Discussions because there are specified participants.

    Direct messages can be sent to a specific participant, group of participants and will only be
    visible to those participants in their conversations.
    """

    participants = models.ManyToManyField(
            Participant,
            related_name='direct_message_exchange_participant',
            help_text='Participants in this direct message exchange.',
        )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    objects = DirectMessageExchangeManager()

    class Meta:
        verbose_name = 'Direct Message Exchange'
        verbose_name_plural = "Direct Message Exchanges"
        ordering = ['-date']

    def __str__(self):

        participant_list = [participant.credit_name for participant in participants]
        return "Direct Message Exchange: { participant_list }".format(
            participant_list = participant_list,
        )

    @property
    def type(self):
        return "Direct Message Exchange"


class DirectMessageManager(models.Manager):
    """ Customer manager for direct messaging."""

    def create_direct_message(self, message, text):
        """Method for quick creation of a direct message."""

        message = self.create(exchange=exchange, author=author, text=text)
        return message


class DirectMessage(models.Manager):
    """Messages in a direct message exhange."""

    author = models.ForeignKey(
        'Participant',
        help_text = 'Participant who authored the message.',
        null=True,
        on_delete = models.SET_NULL,
    )

    exchange = models.ForeignKey(
        'DirectMessageExchange',
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

from django.db import models

from base.models import Participant
# from base.models import EntityOwner

class NoteManager(models.Manager):
    """Custom manager for notes."""

    def create_note(self, participant_owner, entity_owner, title, text, note_type, important):
        """Method for quick creation of a note."""
        note = self.create(participant_owner=participant_owner, entity_owner=entity_owner, title=title, text=text, note_type=note_type, important=important)
        return note


class Note(models.Model):
    """ Basic note."""

    participant_owner = models.ForeignKey(
        Participant,
        help_text = 'Participant who created the note.',
        null = True,
        on_delete = models.SET_NULL,
    )

    # set entity owner for notes associated with orgs, networks, projects, stories
    # so that note persists should the participant leave the platform
    entity_owner = models.OneToOneField(
        'base.EntityOwner',
        help_text = 'Entity that owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    title = models.CharField(
        max_length=255,
    )

    text = models.TextField(
        help_text='Content of the note',
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='When the note was created.'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        help_text='When the note was updated'
    )

    important = models.BooleanField(
        default=False,
        help_text='Mark as important for pinning to top of notes',
    )

    objects = NoteManager()

    def __str__(self):
        return self.title

    @property
    def description(self):
        return self.title

    @property
    def search_title(self):
        return self.title

    @property
    def type(self):
        return "Note"

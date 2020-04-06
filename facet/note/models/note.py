from django.db import models

from base.models import Participant, Anchor


class NoteManager(modfels.Manager):
    """Custom manager for notes."""

    def create_note(self, owner, title, text, note_type, important):
        """Method for quick creation of a note."""
        note = self.create(owner=owner, title=title, text=text, note_type=note_type, important=important)
        return note


class Note(models.Model):
    """ Basic note."""

    # object this is bound to
    anchor = models.OneToOneField(
        Anchor,
        on_delete=models.CASCADE,
        related_name='anchor_object',
        help_text='The anchor object',
    )

    creator = models.ForeignKey(
        Participant,
        help_text = 'Participant who created the note.',
        null = True,
        on_delete = models.SET_NULL,
    )

    # set entity owner for notes associated with orgs, networks, projects, stories
    # so that note persists should the participant leave the platform
    entity_owner = models.OneToOneField(
        EntityOwner,
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

    important = models.BooleanField(
        default=False,
        help_text='Mark as important for pinning to top of notes',
    )

    # FIXME Not sure there is utility for this
    # Choices for Note Type
    # ORGANIZATION = 'ORG'
    # NETWORK = 'NET'
    # USER = 'USER'
    # PROJECT = 'PRO'
    # STORY = 'STO'
    # TASK = 'TSK'
    # EVENT = 'EV'
    #
    # NOTE_TYPE_CHOICES = (
    #     (ORGANIZATION, 'Organization'),
    #     (NETWORK, 'Network'),
    #     (USER, 'Participant'),
    #     (PROJECT, 'Project'),
    #     (STORY, 'Story'),
    #     (TASK, 'Task'),
    #     (EVENT, 'Event'),
    # )
    #
    # # to simplify querying/filtering for notes
    # note_type = models.CharField(
    #     max_length=25,
    #     choices=NOTE_TYPE_CHOICES,
    #     help_text='The kind of object this note is for.'
    # )

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

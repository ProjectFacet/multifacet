from django.db import models

class BaseNetwork(models.Model):
    """A group of organizations.

    A network is a collection of two or more organizations or participant types.
    """

    name = models.CharField(
        max_length=350,
        db_index=True,
        help_text="The identifying name of the network."
    )

    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    description = models.TextField(
        help_text="Short description of the network.",
        blank=True,
    )

    # FIXME Pilkit install
    # logo = models.ImageField(
    #     upload_to='networks',
    #     blank=True,
    # )

    # display_logo = ImageSpecField(
    #     source='logo',
    #     processors=[SmartResize(500, 500)],
    #     format='JPEG',
    # )

    # discussions = GenericRelation(Discussion)

    # notes = GenericRelation(Note)

    # simple assets
    # simple_image_assets = models.ManyToManyField(
    #     'SimpleImage',
    #     blank=True,
    # )
    #
    # simple_document_assets = models.ManyToManyField(
    #     'SimpleDocument',
    #     blank=True,
    # )
    #
    # simple_audio_assets = models.ManyToManyField(
    #     'SimpleAudio',
    #     blank=True,
    # )
    #
    # simple_video_assets = models.ManyToManyField(
    #     'SimpleVideo',
    #     blank=True,
    # )

    class Meta:
        abstract = True
        ordering = ['name']

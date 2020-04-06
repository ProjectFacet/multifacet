from django.db import models

from base.models import Participant
from entity.models import NewsOrganization
from .tag import Tag

class BaseAsset(models.Model):
    """Base class for assets (some metadata)."""

    participant_owner = models.OneToOneField(
        Participant,
        help_text = 'Participant who created/owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    # XXX this means that if a participant from a partner org uploads an asset to another
    # organization's content, that asset will show up in their own organization's library
    # but not the partner organization's library.
    entity_owner = models.OneToOneField(
        EntityOwner,
        help_text = 'Entity that owns this.',
        null = True,
        on_delete = models.SET_NULL,
    )

    title = models.CharField(
        max_length=200,
        help_text='Text for file name. Name it intuitively.',
        blank=True,
    )

    description = models.TextField(
        max_length=300,
        help_text='What is the asset. (If a photo or graphic, it should be the caption.)',
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text='When the asset was created.'
    )

    # TODO: Addition of sensitive status. If an image is added to a Project
    # that is marked sensitive, or to a task or even that are part of senstive Projects,
    # the image should be changed to sensitive.
    # Sensitive images should be excluded from the library and "image add" forms.

    sensitive = models.BooleanField(
        default=False,
        help_text='Is the asset sensitive, or associated with sensitve content?'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    @property
    def search_title(self):
        return self.title


class BaseAssetMetadata(models.Model):
    """Base class for item-attaching asset metadata.

    Used for asset types that are attached to items.
    """

    original = models.BooleanField(
        default=True,
        help_text='This content originally belonged to this entity.'
    )

    attribution = models.TextField(
        max_length=200,
        help_text='The appropriate information for crediting the asset.',
        blank=True,
    )

    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        abstract = True

    # def copy(self):
    #     """Create a copy of an asset for a partner organization in a network.
    #
    #     Copied assets keep all associated information. Organization is set to
    #     the copier's organization and the original flag is set to false.
    #     Triggering a copy also triggers the creation of an asset copy detail record."""
    #
    #     #set the id = None to create the copy of the asset instance
    #     self.id = None
    #     self.original = False
    #     self.save()
    #     return self
    #
    # def get_asset_download_info(self):
    #     """Return rst of asset information for download."""
    #
    #     title = self.title.encode('utf-8')
    #     description = self.description.encode('utf-8')
    #     attribution = self.attribution.encode('utf-8')
    #
    #     if self.type == "ImageAsset" or self.type == "DocumentAsset":
    #         link = "NA"
    #     else:
    #         link = self.link
    #
    #
    #     asset_info="""
    #     {title}\r\n
    #     =======\r\n
    #     Description: {description}\r\n
    #     Attribution: {attribution}\r\n
    #     Link: {link}\r\n
    #     Creation Date: {date}\r\n
    #     Owner: {owner}\r\n
    #     Organization: {organization}\r\n
    #     Original: {original}\r\n
    #     Keywords: {keywords}\r\n
    #     """.format(title=title,
    #             description=description,
    #             attribution=attribution,
    #             link=link,
    #             date=self.creation_date,
    #             owner=self.owner,
    #             organization=self.organization.name,
    #             original=self.original,
    #             keywords=self.keywords,
    #     )
    #
    #     return asset_info

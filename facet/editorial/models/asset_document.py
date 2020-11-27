from django.db import models

from base.models import BaseAssetMetadata, BaseDocument


class DocumentAssetManager(models.Manager):
    """Custom manager for DocumentAsset."""

    def create_documentasset(self, participant_owner, entity_owner, title, description, attribution, document, asset_type):
        """Method for quick creation of a document asset."""
        documentasset=self.create(participant_owner=participant_owner, entity_owner=entity_owner, title=title, description=description, attribution=attribution, document=document, asset_type=asset_type)
        return documentasset


class DocumentAsset(BaseDocument, BaseAssetMetadata):
    """Document Assets (attached to items)"""

    #Choices for Asset type
    PDF = 'PDF'
    WORD = 'WORD DOC'
    TXT =  'TEXT'
    CSV = 'COMMA SEPARATED'
    XLS = 'EXCEL'
    OTHER = 'OTHER'

    ASSET_TYPE_CHOICES = (
        (PDF, 'Adobe PDF'),
        (WORD, 'Word Doc'),
        (TXT, 'Text File'),
        (CSV, 'Comma Separated'),
        (XLS, 'Excel File'),
        (OTHER, 'Other'),
    )

    asset_type = models.CharField(
        max_length=20,
        choices = ASSET_TYPE_CHOICES,
        help_text='The kind of document.'
    )

    # TODO to be populated automatically
    file_type = models.CharField(
        max_length=10,
        help_text='The file extension'
    )

    # TODO to be populated automatically
    file_size = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='Size of uploaded file.'
    )

    objects = DocumentAssetManager()

    def get_document_usage(self):
        """Return items a document is associated with."""
        return self.item_set.all()

    # def get_absolute_url(self):
    #     return reverse('document_asset_detail', kwargs={'pk': self.id})

    @property
    def type(self):
        return "Document Asset"

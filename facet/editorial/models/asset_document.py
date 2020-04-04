# from django.db import models
#
# from base.models import Participant
# from entity.models import NewsOrganization
# from .asset_base import BaseAsset, BaseAssetMetadata
# from .tag import Tag
#
#
# class BaseDocumentAsset(BaseAsset):
#     """Base documents.
#
#     There are subclasses of this for DocumentAssets (attached to items with lots of
#     metadata) and SimpleDocuments (attached to tasks, events, etc).
#     """
#
#     # type name for search system
#     type = "Document"
#
#     document = models.FileField(
#         upload_to='documents',
#         blank=True,
#     )
#
#     class Meta:
#         abstract = True
#
#
# class DocumentAssetManager(models.Manager):
#     """Custom manager for DocumentAsset."""
#
#     def create_documentasset(self, owner, content_object, title, description, attribution, document, asset_type):
#         """Method for quick creation of a document asset."""
#         documentasset=self.create(owner=owner, content_object=content_object, title=title, description=description, attribution=attribution, document=document, asset_type=asset_type)
#         return documentasset
#
#
# class DocumentAsset(BaseDocumentAsset, BaseAssetMetadata):
#     """Document Assets (attached to items)"""
#
#     #Choices for Asset type
#     PDF = 'PDF'
#     WORD = 'WORD DOC'
#     TXT =  'TEXT'
#     CSV = 'COMMA SEPARATED'
#     XLS = 'EXCEL'
#     OTHER = 'OTHER'
#
#     ASSET_TYPE_CHOICES = (
#         (PDF, 'Adobe PDF'),
#         (WORD, 'Word Doc'),
#         (TXT, 'Text File'),
#         (CSV, 'Comma Separated'),
#         (XLS, 'Excel File'),
#         (OTHER, 'Other'),
#     )
#
#     asset_type = models.CharField(
#         max_length=20,
#         choices = ASSET_TYPE_CHOICES,
#         help_text='The kind of document.'
#     )
#
#     objects = DocumentAssetManager()
#
#     def get_document_usage(self):
#         """Return items a document is associated with."""
#         return self.item_set.all()
#
#     # def get_absolute_url(self):
#     #     return reverse('document_asset_detail', kwargs={'pk': self.id})
#
#     @property
#     def type(self):
#         return "DocumentAsset"
#
#
# class SimpleDocument(BaseDocumentAsset):
#     """Simple Document (file upload, attached to events, tasks, etc.)"""
#
#     def get_usage(self):
#         """Return Organizations, Networks, Projects, Events and Tasks
#         the simple asset is associated with."""
#
#         associations = []
#         orgs = self.organization_simple_document.all()
#         networks = self.network_set.all()
#         projects = self.project_set.all()
#         events = self.event_set.all()
#         tasks = self.event_set.all()
#         associations.extend(orgs)
#         associations.extend(networks)
#         associations.extend(projects)
#         associations.extend(events)
#         associations.extend(tasks)
#
#         return associations
#
#
#     # def get_absolute_url(self):
#     #     return reverse('simple_document_detail', kwargs={'pk': self.id})
#
#
#     @property
#     def type(self):
#         return "SimpleDocument"

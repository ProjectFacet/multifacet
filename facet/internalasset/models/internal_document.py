from django.db import models

from base.models import BaseDocument

class InternalDocument(BaseDocument):
    """Simple Document (file upload, attached to events, tasks, etc.)"""

    def get_usage(self):
        """Return Organizations, Networks, Projects, Events and Tasks
        the internal asset is associated with."""

        associations = []
        orgs = self.organization_internal_document.all()
        networks = self.network_set.all()
        projects = self.project_set.all()
        events = self.event_set.all()
        tasks = self.event_set.all()
        associations.extend(orgs)
        associations.extend(networks)
        associations.extend(projects)
        associations.extend(events)
        associations.extend(tasks)

        return associations

    # def get_absolute_url(self):
    #     return reverse('internal_document_detail', kwargs={'pk': self.id})

    @property
    def type(self):
        return "Simple Document"

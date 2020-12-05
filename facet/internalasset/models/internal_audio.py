from django.db import models

from base.models import BaseAudio


class InternalAudio(BaseAudio):
    """Internal Audio that attaches to an event, task, etc."""

    def get_usage(self):
        """Return Organizations, Networks, Projects, Events and Tasks
        the internal asset is associated with."""

        associations = []
        orgs = self.organization_internal_audio.all()
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
    #     return reverse('internal_audio_detail', kwargs={'pk': self.id})

    @property
    def type(self):
        return "Internal Audio"

from django.db import models

from base.models import Participant

class FreelanceManager(models.Model):
    """A team user who manages contract talent."""

    participant = models.OneToOneField(
        Participant,
        on_delete=models.CASCADE,
    )

    # relevant for editors and admins of organizations managing freelancers
    # freelance manager will appear in public search results for editors accepting contact
    # from freelancers
    # freelancer related views sorted by this profile
    public = models.BooleanField(
        default=False,
        help_text='Is this freelance manager publicly listed?',
    )

    class Meta:
        verbose_name = 'Freelance Manager'
        verbose_name_plural = 'Freelance Managers'

    def __str__(self):
        return self.participant.credit_name

    # def get_absolute_url(self):
    #     return reverse('talent_editor_detail', kwargs={'pk': self.id})

    @property
    def search_title(self):
        return self.participant.credit_name

    @property
    def description(self):
        return "Freelance Manager - {participant}/{org}".format(
                                                    participant=self.participant.credit_name,
                                                    org=self.participant.organization,
                                                    )

    @property
    def type(self):
        return "Freelance Manager"

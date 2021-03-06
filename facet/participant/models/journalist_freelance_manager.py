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
        help_text='whether the freelance manager is publicly listed',
    )

    interest = models.TextField(
        help_text = 'Description of stories interested in.',
        blank=True,
    )

    topics = models.TextField(
        help_text = 'Description of topics interested in.',
        blank=True,
    )

    formats = models.TextField(
        help_text = 'Description of formats interested in.',
        blank=True,
    )

    class Meta:
        verbose_name = 'Freelance Manager'
        verbose_name_plural = 'Freelance Managers'

    def __str__(self):
        return self.participant.credit_name

    # def get_absolute_url(self):
    #     return reverse('freelance_manager_detail', kwargs={'pk': self.id})

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

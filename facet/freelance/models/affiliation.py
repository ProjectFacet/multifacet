from django.db import models

from .journalist_freelance import FreelanceJournalist
from .journalist_freelancemanager import FreelanceManager
from entity.models import NewsOrganization
from note.models import Note


class FreelancerAffiliationRecord(models.Model):
    """Information tracked by a news organization about freelancers.

    Basic info like email, bio, skillset, availability, current_location, gear
    are available on FreelanceJournalist.

    The data captured here is for a News Organization's internal
    notes regarding their affiliation with a Freelance Journalist.
    """

    organization = models.ForeignKey(
        NewsOrganization,
        on_delete = models.CASCADE,
    )

    # FIXME Update to allow for newsrooms to keep historical records even if a
    # freelancer has deactivated/deleted their account
    freelancer = models.ForeignKey(
        FreelanceJournalist,
        on_delete = models.CASCADE,
    )

    w9_on_file = models.BooleanField(
        default=False,
        help_text='Does the organization have a W9 on file.',
    )

    rates = models.TextField(
        blank=True,
        help_text='The rates the freelancer is paid by the org.',
    )

    strengths = models.TextField(
        blank=True,
        help_text='Internal notes on strengths of the freelancer.',
    )

    disclosures = models.TextField(
        blank=True,
        help_text='Disclosures regarind any potential noteworthy conflicts of interest.',
    )

    editor_notes = models.TextField(
        blank=True,
        help_text='Any notes for editors on things to know when working with this freelancer.',
    )

    # a freelancer in an organizations freelancer pool can be available
    # for assigning to projects, stories, and tasks through the regular team picker.
    vetted = models.BooleanField(
        default=False,
        help_text='Is this freelancer a trusted regular?',
    )

    status = models.BooleanField(
        default=True,
        help_text='Is this freelancer currently working for the organization?'
    )

    # notes
    notes = models.ManyToManyField(Note, blank=True)

    def __str__(self):
        return "{organization} - {freelancer}".format(
                                        organization=self.organization.name,
                                        freelancer=self.freelancer.participant.credit_name,
                                        )

    class Meta:
        verbose_name = 'Freelancer Affiliation Record'
        verbose_name_plural = 'Freelancer Affiliation Records'
        unique_together = ['organization', 'freelancer']

    @property
    def search_title(self):
        return "{organization} - {freelancer}".format(
                                        organization=self.organization.name,
                                        freelancer=self.freelancer.participant.credit_name,
                                        )

    @property
    def description(self):
        return "Freelancer Affiliation Detail"

    @property
    def type(self):
        return "Freelancer Affiliation Detail"

    # def get_absolute_url(self):
    #     return reverse('freelancer_affiliation_detail', kwargs={'pk': self.id})


class OrganizationAffiliationRecord(models.Model):
    """Information tracked about an organization by a freelancer.

    The data captured here is for a freelancer's records regarding
    their affiliation with a NewsOrganization.
    """

    organization = models.ForeignKey(
        NewsOrganization,
        on_delete = models.CASCADE,
    )

    freelancer = models.ForeignKey(
        FreelanceJournalist,
        on_delete = models.CASCADE,
    )

    contacts = models.ManyToManyField(
        FreelanceManager,
        related_name='affilation_contact',
        help_text='News Organization Freelance Managers freelancer works with.',
        blank=True,
    )

    details = models.TextField(
        blank=True,
        help_text='Any notes for freelancer to remember about this affiliation.',
    )

    favorite = models.BooleanField(
        default=False,
        help_text='Is this news organization a favored contract?',
    )

    # notes
    notes = models.ManyToManyField(Note, blank=True)

    def __str__(self):
        return "{organization} - {freelancer}".format(
                                        organization=self.organization.name,
                                        freelancer=self.freelancer.participant.credit_name,
                                        )

    class Meta:
        verbose_name = 'News Organization Affiliation Record'
        verbose_name_plural = 'News Organization Affiliation Records'
        unique_together = ['organization', 'freelancer']

    # def get_absolute_url(self):
    #     return reverse('freelancer_affiliation_detail', kwargs={'pk': self.id})

    @property
    def search_title(self):
        return "{organization} - {freelancer}".format(
                                        organization=self.organization.name,
                                        freelancer=self.freelancer.participant.credit_name,
                                        )

    @property
    def description(self):
        return "News Organization Affiliation Detail"

    @property
    def type(self):
        return "News Organization Affiliation Detail"

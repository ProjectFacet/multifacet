from django.db import models

class PartnerManager(models.Manager):
    """Custom manager for Partner."""

    def create_partner_record(self, partner_type, partner_name, partner_id):
        """Method that takes in type, name and id for quick access."""

        partner = self.create(partner_type=partner_type, partner_name=partner_name, partner_id=partner_id)
        return partner


class Partner(models.Model):
    """Facilitates inclusion of multiple kinds of entities as partners in
    partner_with M2M field on projects, stories, etc.

    Models that can be Partners:
    _Organization, Participant

    Models that select partner_with partners:
    Project, Story +

    Models that are partners point at an Partner record as the
    partner_profile

    Collaborative models point to Partner records through partner_with.

    Ex. A NewsOrganization has partner record and a Project is collaborative.
    Project has a field called partner_with that is a M2M with Partner.

    This allows for consistency across multiple kinds of Partners.

    Additional internal information is included on the record for easy access.
    """

    # TODO Need for passthrough table to denote whether a partner is active for
    # an organization. Need: When participant deletes there account, need to
    # maintain data integrity regarding their involvement with content.

    # Choices for Partner Type
    PARTICIPANT = 'PARTICIPANT'
    NEWSORGANIZATION = 'NEWS ORGANIZATION'
    NEWSORGANIZATIONNETWORK = 'NEWS ORGANIZATION NETWORK'


    PARTNER_TYPE_CHOICES = (
        (PARTICIPANT, 'Participant'),
        (NEWSORGANIZATION, 'News Organization'),
        (NEWSORGANIZATIONNETWORK, 'News Organization Network'),
    )

    partner_type = models.CharField(
        max_length=250,
        choices=PARTNER_TYPE_CHOICES,
        help_text='What kind of partner it is.',
    )

    partner_name = models.CharField(
        max_length=250,
        help_text='Name of the partner.',
    )

    partner_id = models.PositiveIntegerField()

    objects = PartnerManager()

    class Meta:
        verbose_name = 'Partner Profile'
        verbose_name_plural = "Partner Profiles"

    def __str__(self):
        return self.partner_name

    @property
    def description(self):
        return "Partner Profile for {partner_type} {partner_name} ({partner_id})".format(
            partner_type=self.partner_type,
            partner_name=self.partner_name,
            partner_id=self.partner_id,
        )

    @property
    def type(self):
        return "Partner Profile"


    def get_copied_content(self):
        """Returns queryset of content picked up from a partner."""

        if self.newsorganization:
            copied_content = self.newsorganization.get_copied_content()
            return copied_content
        if self.newsorganizationnetwork:
            copied_content = self.newsorganizationnetwork.get_copied_content()
            return copied_content
        if self.participant:
            copied_content = self.participant.get_copied_content()
            return copied_content

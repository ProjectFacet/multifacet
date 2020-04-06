from django.db import models

from entity.models import NewsOrganization


class NewsOrganizationSubscriptionManager(models.Manager):
    """Custom manager for NewsOrganizationSubscription."""

    def create_subscription(self, newsorganization, collaborations, contractors):
        """Method for quick creation of subscription."""

        subscription = self.create(
                        newsorganization=newsorganization,
                        collaborations=collaborations,
                        contractors=contractors,
                        partner_discovery=partner_discovery,
                        )
        return subscription



class NewsOrganizationSubscription(models.Model):
    """Details of a news organization subscription."""

    newsorganization = models.OneToOneField(
        NewsOrganization,
        help_text='Organization associated with this subscription if Org subscription type.',
        on_delete=models.CASCADE,
    )

    # Organization functionality
    collaborations = models.BooleanField(
        default=False,
        help_text='The organization is using the account for base features of editorial workflow, project management and collaboration.',
    )

    freelance_management = models.BooleanField(
        default=False,
        help_text='The organization is using the account to manage contractors.',
    )

    partner_discovery = models.BooleanField(
        default=True,
        help_text='Base level subscription. Allows organization to be publicly listed for search as a potential collaborative partner. Allows org users to see other publicly listed orgs.',
    )

    objects = NewsOrganizationSubscriptionManager()

    def __str__(self):
        return "Organization Subscription - {organization}".format(organization=self.organization.name)

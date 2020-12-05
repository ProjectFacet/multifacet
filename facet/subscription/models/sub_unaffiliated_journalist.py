from django.db import models

from participant.models import UnaffiliatedStaffJournalist


class UnaffiliatedStaffJournalistSubscriptionManager(models.Manager):
    """Custom manager for an unaffiliated staff journalist subscription."""

    def create_subscription(self, user, standard):
        """Method for quick creation of subscription."""

        subscription = self.create(
                        journalist=journalist,
                        standard=standard,
                        )

        return subscription


class UnaffiliatedStaffJournalistSubscription(models.Model):
    """Details of an unaffiliated staff journalist subscription."""

    journalist = models.ForeignKey(
        UnaffiliatedStaffJournalist,
        help_text='Unaffiliated staff journalist associated with this subscription.',
        on_delete=models.CASCADE,
    )

    objects = StaffJournalistSubscriptionManager()

    def __str__(self):
        return "Unaffiliated Staff Journalist Subscription - {journalist}".format(journalist=self.journalist.credit_name)

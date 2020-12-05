from django.db import models

from participant.models import StaffJournalist


class StaffJournalistSubscriptionManager(models.Manager):
    """Custom manager for staff journalist subscription."""

    def create_subscription(self, user, standard):
        """Method for quick creation of subscription."""

        subscription = self.create(
                        journalist=journalist,
                        standard=standard,
                        )

        return subscription


class StaffJournalistSubscription(models.Model):
    """Details of a staff journalist subscription."""

    journalist = models.ForeignKey(
        StaffJournalist,
        help_text='Affiliated staff journalist associated with this subscription.',
        on_delete=models.CASCADE,
    )

    objects = StaffJournalistSubscriptionManager()

    def __str__(self):
        return "Affiliated Staff Journalist Subscription - {journalist}".format(journalist=self.journalist.credit_name)

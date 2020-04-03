# from django.db import models
#
# from entity.models import NewsOrganization
# from base.models import Participant
# from freelance.models import FreelanceJournalist
#
#
# class FreelanceSubscriptionManager(models.Manager):
#     """Custom manager for freelancer subscription."""
#
#     def create_subscription(self, user, standard):
#         """Method for quick creation of subscription."""
#
#         subscription = self.create(
#                         user=user,
#                         standard=standard,
#                         )
#
#         return subscription
#
#
# @python_2_unicode_compatible
# class FreelanceSubscription(models.Model):
#     """Details of a freelancer subscription.
#
#     """
#
#     freelancer = models.ForeignKey(
#         FreelanceJournalist,
#         help_text='Freelancer associated with this subscription.',
#         on_delete=models.CASCADE,
#     )
#
#     objects = FreelanceSubscriptionManager()
#
#     def __str__(self):
#         return "Freelance Subscription - {freelancer}".format(freelancer=self.freelancer.credit_name)

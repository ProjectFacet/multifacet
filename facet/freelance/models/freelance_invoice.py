# from django.db import models
#
# from .journalist_freelance import FreelanceJournalist
# from .journalist_talenteditor import FreelanceManager
# from entity.models import NewsOrganization
#
# from base.models import BaseInvoice
#
#
# class FreelanceInvoice(BaseInvoice):
#     """Invoice for freelance assignment(s)"""
#
#     freelancer = models.ForeignKey(
#         'FreelanceJournalist',
#         on_delete = models.CASCADE,
#     )
#
#     manager = models.ForeignKey(
#         'FreelanceManager',
#         help_text='Manager responsible for this assignment.',
#         on_delete = models.CASCADE,
#     )
#
#     organization = models.ForeignKey(
#         'NewsOrganization',
#         help_text='Organization that owns this assignment.',
#         on_delete = models.CASCADE,
#     )
#
#     class Meta:
#         verbose_name = 'Freelance Invoice'
#         verbose_name_plural = 'Freelance Invoices'
#
#     def __str__(self):
#         return self.reference_code
#
#     # def get_absolute_url(self):
#     #     return reverse('invoice_detail', kwargs={'pk': self.id})
#
#     @property
#     def search_title(self):
#         return self.reference_code
#
#     @property
#     def description(self):
#         return self.text
#
#     @property
#     def type(self):
#         return 'Freelance Invoice'

# from django.db import models
#
# from participant.models import Participant
#
# class FreelanceJournalist(models.Model):
#     """A Participant who is a freelancer.
#
#     Profile that tracks additional information about the participant as a
#     contractor.
#     """
#
#     participant = models.OneToOneField(
#         'Participant',
#         on_delete=models.CASCADE,
#     )
#
#     resume = models.FileField(
#         upload_to='resumes/%Y/%m/%d',
#         blank=True,
#         null=True,
#         help_text='PDF of contractor resume.',
#     )
#
#     address = models.TextField(
#         blank=True,
#         help_text='Mailing address.',
#     )
#
#     availability = models.TextField(
#         help_text="Notes on when a contractor is available or not.",
#         blank=True,
#     )
#
#     # differs from participant.location
#     # participant.location is intended as general base. ie. San Francisco
#     # current_location is intended for finding contractors that are near
#     # a newsworthy thing. ie. "Berkely Campus" during a protest
#     current_location = models.TextField(
#         help_text="Freelancer's specific location.",
#         blank=True,
#     )
#
#     gear = models.TextField(
#         help_text="Gear that a contractor has access to and skills for.",
#         blank=True,
#     )
#
#     # contractors will appear in public search results for contractors accepting work
#     public = models.BooleanField(
#         default=True,
#         help_text='Is the contractor publicly listed?',
#     )
#
#     portfolio_link1 = models.URLField(
#         max_length=500,
#         help_text='Link to portfolio item.',
#         blank=True,
#         null=True,
#     )
#
#     portfolio_link2 = models.URLField(
#         max_length=500,
#         help_text='Link to portfolio item.',
#         blank=True,
#         null=True,
#     )
#
#     portfolio_link3 = models.URLField(
#         max_length=500,
#         help_text='Link to portfolio item.',
#         blank=True,
#         null=True,
#     )
#
#
#     class Meta:
#         verbose_name = "Freelance Journalist"
#         verbose_name_plural = "Freelance Journalists"
#
#
#     def __str__(self):
#         return self.participant.credit_name
#
#     # def get_absolute_url(self):
#     #     return reverse('participant_detail', kwargs={'pk': self.id})
#
#     @property
#     def search_title(self):
#         return self.participant.credit_name
#
#     @property
#     def description(self):
#         return "{participant}, {title}".format(
#                                         participant=self.participant.credit_name,
#                                         title="Freelance Journalist",
#                                         )
#
#     @property
#     def type(self):
#         return "Freelance Journalist"
#
#
#     # def get_active_assignments(self):
#     #     """Return all active assignment."""
#     #     return self.assignment_set.filter(complete=False)
#     #
#     #
#     # def get_active_pitches(self):
#     #     """Return all active assignment."""
#     #     return self.pitch_set.filter(Q(status="Pitched")|Q(status="Accepted"))

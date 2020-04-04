# from django.db import models
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
#
# class ClientProfile(models.Model):
#     """
#         Profile information for a client organization that is participating in a
#         licensing/financial transaction as opposed to a collaborative one.
#     """
#
#     pass
#
#     # TODO
#     # contenttyptes / generic relation to different organization types: NewsOrganization and TBD
#
#     # organization = models.OneToOne(
#     #     ContentType
#     # )
#     #
#     # object_id = models.PositiveIntegerField()
#     # content_object = GenericForeignKey('content_type', 'object_id')
#     #
#     # class Meta:
#     #     verbose_name = 'Client Profile'
#     #     verbose_name_plural = 'Client Profiles'

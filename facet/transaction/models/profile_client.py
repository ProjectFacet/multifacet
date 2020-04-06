from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ClientProfile(models.Model):
    """
        Profile information for a client organization that is participating in a
        licensing/financial transaction as opposed to a collaborative one.
    """

    pass

    ## Anchor relation to different organization types: NewsOrganization and TBD

    ## object this is bound to
    # anchor = models.OneToOneField(
    #     Anchor,
    #     on_delete=models.CASCADE,
    #     related_name='anchor_object',
    #     help_text='The anchor object',
    # )

    # class Meta:
    #     verbose_name = 'Client Profile'
    #     verbose_name_plural = 'Client Profiles'

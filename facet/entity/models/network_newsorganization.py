# from django.db import models
#
# # from entity.models import NewsOrganization
# from base.models import BaseNetwork
#
# class NewsOrganizationNetwork(BaseNetwork):
#     """A group of organizations.
#
#     A network is a collection of two or more organizations seeking to create a sharing
#     or collaborating relationship.
#
#     Sharing means the source organization has made the content available to other
#     members of the network.
#
#     An organization can opt to collaborate with one of more members of a Network.
#     Collaboration means that a user from a collaborating organization can participate
#     in the editorial process on the host organization's content. They can edit, upload
#     assets and participate in any relevant discussions.
#     """
#
#     # owner_newsorganization = models.ForeignKey(
#     #     NewsOrganization,
#     #     null=True,
#     #     on_delete = models.SET_NULL,
#     #     help_text='News organization that owns the network.',
#     # )
#     #
#     # members = models.ManyToManyField(
#     #     NewsOrganization,
#     #     related_name='network_newsorganization',
#     # )
#
#     class Meta:
#         verbose_name = 'Network'
#         verbose_name_plural = "Networks"
#         ordering = ['name']
#
#     def __str__(self):
#         return self.name
#
#     @property
#     def description(self):
#         return "{description}".format(description=self.description)
#
#     @property
#     def search_title(self):
#         return self.name
#
#     @property
#     def type(self):
#         return "Network"
#
#     # def get_absolute_url(self):
#     #     return reverse('network_detail', kwargs={'pk': self.id})
#
#     # def get_network_shared_stories(self):
#     #     """ Return list of stories shared with a network.
#     #
#     #     This is used to populate the network content dashboard.
#     #     """
#     #
#     #     from .story import Story
#     #
#     #     network_stories = Story.objects.filter(Q(share_with=self))
#     #     return network_stories

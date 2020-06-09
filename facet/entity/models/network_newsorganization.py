from django.db import models
from django.db.models import Q

from base.models import BaseNetwork, NetworkMember
from .organization_news import NewsOrganization

class NewsOrganizationNetwork(BaseNetwork):
    """A group of organizations.

    A network is a collection of two or more organizations seeking to create a sharing
    or collaborating relationship.

    Sharing means the source organization has made the content available to other
    members of the network.

    An organization can opt to collaborate with one of more members of a Network.
    Collaboration means that a user from a collaborating organization can participate
    in the editorial process on the host organization's content. They can edit, upload
    assets and participate in any relevant discussions.
    """

    members = models.ManyToManyField(
        NetworkMember,
        related_name='network_members',
        blank=True,
    )

    class Meta:
        verbose_name = 'News Organization Network'
        verbose_name_plural = "News Organization Networks"
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def description(self):
        return "{description}".format(description=self.description)

    @property
    def search_title(self):
        return self.name

    @property
    def type(self):
        return "Network"

    # def get_absolute_url(self):
    #     return reverse('network_detail', kwargs={'pk': self.id})

    #FIXME Consider how a network may be a member or partner to others
    def get_partner_vocab(self):
        """
        Returns partner_profiles of networks, entities and participents eligible for partnering.
        Any Network the NewsOrganizationNetwork is a partner of.
        """

        # connections_and_networks = []
        # connections = self.connections
        # networks = NewsOrganizationNetwork.get_networks(self)
        # network_partner_profiles = [network.partner_profile for network in networks]
        # connections_and_networks.extend(connections)
        # connections_and_networks.extend(network_partner_profiles)
        return []


    def convert_members_to_partners(self):
        """Retrieve partner_profiles of a network's members."""

        # get network members
        members = self.member_set.all()
        # get network member actuals
        newsorganizations = [member.newsorganization for member in members]
        # get partner_profiles of member actuals
        # partner_profiles = [newsorganization.partner_profile for newsorganization in newsorganizations]
        partner_profiles = Partner.objects.filter(Q(self.newsorganization__in==newsorganizations))

        return partner_profiles


    def get_associated_newsorganizations(self):
        """Return member newsorganizations and owners."""

        return NewsOrganization.objects.filter(Q(network_member_profile__in=self.members) | Q(entity_owner_profile=self.entity_owner))


    def get_projects(self):
        """Retrieve projects owned by a news organization network."""

        return Project.objects.filter(entity_owner=self.entity_owner_profile)


    def get_collaborative_projects(self):
        """Retrieve collaborative projects owned by another entity but partnered
        on."""

        return Project.objects.filter(partner_with=self.partner_profile)


    def get_item_templates(self):
        """Return queryset of item templates that should be available."""

        from editorial.models import ItemTemplate

        return ItemTemplate.objects.filter(Q(sitewide=True) | Q(entity_owner=self.entity_owner_profile) & Q(is_active=True))


    def get_image_library(self):
        """Retrieve appropriate image library."""

        return ImageAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner

    def get_document_library(self):
        """Retrieve appropriate document library."""

        return DocumentAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner

    def get_audio_library(self):
        """Retrieve appropriate audio library."""

        return AudioAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner

    def get_video_library(self):
        """Retrieve appropriate video library."""

        return VideoAsset.objects.filter(entity_owner==self.entity_owner_profile)
        # FIXME account for visibility of library to partner



    # def get_network_shared_stories(self):
    #     """ Return list of stories shared with a network.
    #
    #     This is used to populate the network content dashboard.
    #     """
    #
    #     from .story import Story
    #
    #     network_stories = Story.objects.filter(Q(share_with=self))
    #     return network_stories

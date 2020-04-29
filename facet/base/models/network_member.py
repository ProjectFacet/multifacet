from django.db import models

class NetworkMemberManager(models.Manager):
    """Custom manager for EntityOwner."""

    def create_network_member_record(self, member_type, member_name, member_id):
        """Method that takes in type, name and id for quick access."""

        network_member = self.create(member_type=member_type, member_name=member_name, member_id=member_id)
        return network_member


class NetworkMember(models.Model):
    """Connection between different types of entities participating in a network.

    Different kinds of Participants, Organizations and future entities
    can be members of a Network.

    Models that can be members point at a NetworkMember record as the
    network_member_profile

    Network models point to members in a M2M to capture the members.

    Ex. A Network wants to include two different kinds of organizations
    so the members field is a many2Many with NetworkMember allowing for any
    model with a member_profile FK to be included.

    This allows for consistency across multiple kinds of NetworkMembers.
    """

    # Choices for Member Type
    NEWSORGANIZATION = 'NEWSORGANIZATION'

    MEMBER_TYPE_CHOICES = (
        (NEWSORGANIZATION, 'News Organization'),
    )

    member_type = models.CharField(
        max_length=250,
        choices=MEMBER_TYPE_CHOICES,
        help_text='What kind of member it is.',
    )

    member_name = models.CharField(
        max_length=250,
        help_text='Name of the member.',
    )

    member_id = models.PositiveIntegerField()

    objects = NetworkMemberManager()

    class Meta:
        verbose_name = 'Member Profile'
        verbose_name_plural = "Member Profiles"

    def __str__(self):
        return self.member_name

    @property
    def description(self):
        return "Member Profile for {member_type} {member_name} ({member_id})".format(
            member_type=self.member_type,
            member_name=self.member_name,
            member_id=self.member_id,
        )

    @property
    def type(self):
        return "Member Profile"

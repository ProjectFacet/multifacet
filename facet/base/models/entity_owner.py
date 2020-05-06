from django.db import models

class EntityOwnerManager(models.Manager):
    """Custom manager for EntityOwner."""

    def create_entity_owner_record(self, owner_type, owner_name, owner_id):
        """Method that takes in type, name and id for quick access."""

        entity_owner = self.create(owner_type=owner_type, owner_name=owner_name, owner_id=owner_id)
        return entity_owner


class EntityOwner(models.Model):
    """Connection between different types of entities and objects they own.

    Different kinds of organizations and networks can be owners of
    Project, Story, Item, ItemTemplates

    _Organizations and _Networks point at an EntityOwner record as the
    entity_owner_profile

    Owned models point to EntityOwner records as the owner.

    Ex. A NewsOrganization has an EntityOwner record, a project owned by that
    news organization has a field called entity_owner that points to that
    EntityOwner record.

    This allows for consistency across multiple kinds of EntityOwners.
    """

    # Choices for Owner Type
    NEWSORGANIZATION = 'NEWSORGANIZATION'
    NEWSORGANIZATIONNETWORK = 'NEWSORGANIZATIONNETWORK'

    OWNER_TYPE_CHOICES = (
        (NEWSORGANIZATION, 'News Organization'),
        (NEWSORGANIZATIONNETWORK, 'News Organization Network'),
    )

    owner_type = models.CharField(
        max_length=250,
        choices=OWNER_TYPE_CHOICES,
        help_text='What kind of entity it is.'
    )

    owner_name = models.CharField(
        max_length=250,
        help_text='Name of the entity',
    )

    owner_id = models.PositiveIntegerField()

    objects = EntityOwnerManager()

    class Meta:
        verbose_name = 'Entity Owner Profile'
        verbose_name_plural = "Entity Owner Profiles"

    def __str__(self):
        return self.owner_name

    @property
    def description(self):
        return "Owner Profile for {owner_type} {owner_name} ({owner_id})".format(
            owner_type=self.owner_type,
            owner_name=self.owner_name,
            owner_id=self.owner_id,
        )

    @property
    def type(self):
        return "Entity Owner Profile"


    def get_partners_vocab(self):
        """Retrieve appropriate partners for the entity."""

        if self.newsorganization:
            partners = self.newsorganization.get_partners_vocab()
            return partners

        if self.newsorganizationnetwork:
            partners = self.newsorganizationnetwork.get_partners_vocab()
            return partners

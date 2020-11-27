"""
Base Abstract Models for use across other apps.

Place abstract base models in this file and import/subclass
in apps where needed.

Participant(AbstractUser) included as base user profile.
Extension profiles in other apps reference with OneToOne

Base Abstract Model Example

BaseOrganization
    entity.models.NewsOrganization(BaseOrganization)
    entity.models.ClientOrganization(BaseOrganization)

BaseNetwork
    entity.models.NewsNetwork(BaseNetwork)

BaseInvoice
    freelance.models.FreelancerInvoice(BaseInvoice)

---------------------------
Base Abstract Models:
---------------------------
Participant(AbstractUser)
BaseOrganization
BaseNetwork
BaseInvoice

"""

from .participant import Participant

from .base_organization import BaseOrganization
from .base_network import BaseNetwork
from .base_invoice import BaseInvoice

from .entity_owner import EntityOwner
from .anchor import Anchor
from .partner import Partner
from .network_member import NetworkMember

from .base_asset import BaseAsset, BaseAssetMetadata
from .base_asset import BaseAudio, BaseDocument, BaseImage, BaseVideo

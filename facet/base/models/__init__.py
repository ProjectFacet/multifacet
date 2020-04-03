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
# from .base_organization import BaseOrganization
# from .base_network import BaseNetwork
# from .base_invoice import BaseInvoice

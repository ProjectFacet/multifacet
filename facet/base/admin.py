from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Participant

# from .entity_owner import EntityOwner
# from .anchor import Anchor
# from .partner import Partner
# from .network_member import NetworkMember

admin.site.register(Participant, UserAdmin)

# admin.site.register(EntityOwner)
# admin.site.register(Anchor)
# admin.site.register(Partner)
# admin.site.register(NetworkMember)

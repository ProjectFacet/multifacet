from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Participant

from .models import EntityOwner
from .models import Anchor
from .models import Partner
from .models import NetworkMember

admin.site.register(Participant, UserAdmin)

admin.site.register(EntityOwner)
admin.site.register(Anchor)
admin.site.register(Partner)
admin.site.register(NetworkMember)

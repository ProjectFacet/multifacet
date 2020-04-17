from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import Participant

from .models import EntityOwner
from .models import Anchor
from .models import Partner
from .models import NetworkMember


class ParticipantChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Participant
        fields = "__all__"

@admin.register(Participant)
class ParticipantAdmin(UserAdmin):
    form = ParticipantChangeForm
    fieldsets = UserAdmin.fieldsets + (("Facet", {'fields': (
        'display_name',
        'credit_name',
        'name_pronunciation',
        'pronoun',
        'title',
        'phone',
        'biography',
        'city',
        'postal_code',
        'expertise',
    )}), )


admin.site.register(EntityOwner)
admin.site.register(Anchor)
admin.site.register(Partner)
admin.site.register(NetworkMember)

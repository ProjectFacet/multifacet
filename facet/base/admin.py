from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Participant

admin.site.register(Participant, UserAdmin)

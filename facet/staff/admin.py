from django.contrib import admin

from .models import StaffJournalist, UnaffiliatedStaffJournalist

admin.site.register(StaffJournalist)
admin.site.register(UnaffiliatedStaffJournalist)

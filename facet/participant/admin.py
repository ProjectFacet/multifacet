from django.contrib import admin


from .models import StaffJournalist
from .models import UnaffiliatedStaffJournalist
from .models import FreelanceJournalist
from .models import FreelanceManager



admin.site.register(StaffJournalist)
admin.site.register(UnaffiliatedStaffJournalist)
admin.site.register(FreelanceJournalist)
admin.site.register(FreelanceManager)

from django.contrib import admin

from .models import FreelanceJournalist
from .models import FreelanceManager
from .models import FreelancerAffiliationRecord
from .models import OrganizationAffiliationRecord
from .models import Call
from .models import Pitch
from .models import Assignment
from .models import FreelanceInvoice


admin.site.register(FreelanceJournalist)
admin.site.register(FreelanceManager)
admin.site.register(FreelancerAffiliationRecord)
admin.site.register(OrganizationAffiliationRecord)
admin.site.register(Call)
admin.site.register(Pitch)
admin.site.register(Assignment)
admin.site.register(FreelanceInvoice)

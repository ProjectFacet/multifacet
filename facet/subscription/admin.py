from django.contrib import admin

from .models import NewsOrganizationSubscription
from .models import FreelanceSubscription

admin.site.register(NewsOrganizationSubscription)
admin.site.register(FreelanceSubscription)

"""Facet URL Configuration """


from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('', include('base.urls')),
    # path('', include('editorial.urls')),
    # path('', include('entity.urls')),
    # path('', include('freelance.urls')),
    # path('', include('staff.urls')),
    # path('', include('subscription.urls')),
    # path('', include('transaction.urls')),
    # path('', include('task.urls')),
    # path('', include('timeline.urls')),
    # path('', include('social.urls')),
    # path('', include('note.urls')),
    # path('', include('data.urls')),
    # path('', include('engagement.urls')),
    # path('', include('pickup.urls')),
    # path('', include('dei.urls')),
    # path('', include('pavilion.urls')),
    # path('', include('glassbreak.urls')),
    # path('', include('formation.urls')),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
]

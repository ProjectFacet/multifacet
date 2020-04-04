"""Facet URL Configuration """


from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('base/', include('base.urls')),
    path('editorial/', include('editorial.urls')),
    path('entity/', include('entity.urls')),
    path('freelance/', include('freelance.urls')),
    path('staff/', include('staff.urls')),
    path('subscription/', include('subscription.urls')),
    path('transaction/', include('transaction.urls')),
    path('task/', include('task.urls')),
    path('timeline/', include('timeline.urls')),
    path('social/', include('social.urls')),
    path('note/', include('note.urls')),
    path('data/', include('data.urls')),
    path('engagement/', include('engagement.urls')),
    path('pickup/', include('pickup.urls')),
    path('dei/', include('dei.urls')),
    path('admin/', admin.site.urls),
]

"""facet URL Configuration """


from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('editorial/', include('editorial.urls')),
    path('admin/', admin.site.urls),
]

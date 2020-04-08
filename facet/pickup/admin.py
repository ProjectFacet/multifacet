from django.contrib import admin

from .models import StoryPickupDetail
from .models import ItemPickupDetail
from .models import ImagePickupDetail
from .models import DocumentPickupDetail
from .models import AudioPickupDetail
from .models import VideoPickupDetail

admin.site.register(StoryPickupDetail)
admin.site.register(ItemPickupDetail)
admin.site.register(ImagePickupDetail)
admin.site.register(DocumentPickupDetail)
admin.site.register(AudioPickupDetail)
admin.site.register(VideoPickupDetail)

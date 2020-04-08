from django.contrib import admin

from .models import Project
from .models import Story
from .models import ItemTemplate
from .models import Item
from .models import ImageAsset, SimpleImage
from .models import DocumentAsset, SimpleDocument
from .models import AudioAsset, SimpleAudio
from .models import VideoAsset, SimpleVideo
from .models import Tag
from .models import ContentLicense
from .models import Correction
from .models import Update


admin.site.register(Project)
admin.site.register(Story)
admin.site.register(ItemTemplate)
admin.site.register(Item)
admin.site.register(ImageAsset)
admin.site.register(SimpleImage)
admin.site.register(DocumentAsset)
admin.site.register(SimpleDocument)
admin.site.register(AudioAsset)
admin.site.register(SimpleAudio)
admin.site.register(VideoAsset)
admin.site.register(SimpleVideo)
admin.site.register(Tag)
admin.site.register(ContentLicense)
admin.site.register(Correction)
admin.site.register(Update)

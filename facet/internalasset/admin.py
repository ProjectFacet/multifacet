from django.contrib import admin

from .models import InternalImage
from .models import InternalDocument
from .models import InternalAudio
from .models import InternalVideo


admin.site.register(InternalImage)
admin.site.register(InternalDocument)
admin.site.register(InternalAudio)
admin.site.register(InternalVideo)

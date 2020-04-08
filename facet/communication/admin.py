from django.contrib import admin

from .models import Discussion
from .models import Comment
from .models import DirectMessageExchange
from .models import DirectMessage

admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(DirectMessageExchange)
admin.site.register(DirectMessage)

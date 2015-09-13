from django.contrib import admin
from blog.models import Post, ContentText, ContentImage, ContentVoice

admin.site.register(Post)

admin.site.register(ContentText)
admin.site.register(ContentImage)
admin.site.register(ContentVoice)

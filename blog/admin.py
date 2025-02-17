from django.contrib import admin
from .models import Post
from embed_video.admin import AdminVideoMixin

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

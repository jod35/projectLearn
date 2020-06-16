from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'publish', 'created', 'author')
    list_filter = ('publish', 'created')
    search_fields = ('author', 'title')

from django.contrib import admin
from .models import Post,Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'publish', 'created', 'author')
    list_filter = ('publish', 'created')
    search_fields = ('author', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('author','body','commented_on')
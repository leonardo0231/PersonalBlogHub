from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_at', 'update_at')
    ordering = ('title', 'author', 'create_at')
    list_filter = ('author', 'create_at')
    search_fields = ('title', 'author')
    readonly_fields = ('create_at',)


class AdminComment(admin.ModelAdmin):
    list_display = ('post', 'user')
    list_filter = ('post', 'user', 'create_at')
    search_fields = ('post', 'user')


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
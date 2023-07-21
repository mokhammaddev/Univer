from django.contrib import admin
from .models import Post, Comment, Body


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']


@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    list_display = ['id', 'body']
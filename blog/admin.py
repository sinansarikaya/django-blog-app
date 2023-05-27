from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    list_display_links = ['title']
    search_fields = ["title", "content"]
    list_filter = ["created_at", "updated_at"]
    list_per_page = 25
    date_hierarchy = "created_at"
    ordering = ["-created_at", "title"]
    readonly_fields = ["created_at"]

    class Meta:
        model: Post

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at', 'is_approved']
    list_display_links = ['post']
    list_editable = ["is_approved"]   
    search_fields = ["text", "author"]
    list_filter = ["is_approved", "created_at"]
    ordering = ["-created_at"]
    readonly_fields = ["created_at"]

    class Meta:
        model: Comment
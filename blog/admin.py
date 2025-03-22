from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "image", "is_published")
    list_filter = ("title",)
    search_fields = ("title",)

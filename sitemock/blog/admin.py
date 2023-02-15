from django.contrib import admin

from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "published_date", "slug", "id")
    search_fields = ("title", "text", "slug")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

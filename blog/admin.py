from django.contrib import admin

from .models import (
    Post,
)

@admin.decorators.register(Post)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
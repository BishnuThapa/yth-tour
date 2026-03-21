from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'created_at', 'updated_at']

    def image_preview(self, obj):
        if obj.image_optimized:
            return format_html('<img src="{}" width="70" />', obj.image_optimized.url)
        return "-"
    image_preview.short_description = 'Preview'

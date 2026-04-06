from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1

@admin.register(DayTour)
class DayTourAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title', ]
    }
    list_display = ('title', 'image_preview', 'is_active', 'created_at')
    list_editable = ('is_active',)
    inlines = (GalleryInline,)

    def image_preview(self, obj):
        if obj.image_optimized:
            return format_html('<img src="{}" width="150" />', obj.image_optimized.url)
        return "-"
    image_preview.short_description = 'Preview'
    

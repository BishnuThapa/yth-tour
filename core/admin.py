from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple
from django.utils.html import format_html
from .models import *
# Register your models here.


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title', ]
    }
    list_display = ('title', 'image_preview',
                    'ordering', 'is_active', 'created_at')
    list_editable = ('is_active',)

    def image_preview(self, obj):
        if obj.image_optimized:
            return format_html('<img src="{}" width="70" />', obj.image_optimized.url)
        return "-"
    image_preview.short_description = 'Preview'

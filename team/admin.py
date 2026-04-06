from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.


# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['title', 'thumbnail']

#     def thumbnail(self, object):
#         return format_html('<img src="{}" width="150" height="100" style="border-radius:10%;" />'.format(object.image.url))


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_preview', 'designation', 'ordering']
    list_editable = ['designation', 'ordering']
    prepopulated_fields = {
        'slug': ['name', ]
    }
    # def thumbnail(self, object):
    #     return format_html('<img src="{}" width="100" height="100" style="border-radius:10%;" />'.format(object.image.url))
    def image_preview(self, obj):
        if obj.image_optimized:
            return format_html('<img src="{}" width="70" />', obj.image_optimized.url)
        return "-"
    image_preview.short_description = 'Preview'

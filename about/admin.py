from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.


# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['title', 'thumbnail']

#     def thumbnail(self, object):
#         return format_html('<img src="{}" width="150" height="100" style="border-radius:10%;" />'.format(object.image.url))


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description',
                    'image_preview','created_at', 'updated_at']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image_optimized:
            return format_html('<img src="{}" width="150" />', obj.image_optimized.url)
        return "-"
    image_preview.short_description = 'Preview'
    
admin.site.register(WhyUs)


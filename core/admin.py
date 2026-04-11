from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple
from django.utils.html import format_html
from .models import *
# Register your models here.


class Gallery(admin.TabularInline):
    model = Gallery
    extra = 1


class Itinerary(admin.TabularInline):
    model = Itinerary
    extra = 0

class Faq(admin.TabularInline):
    model = Faq
    extra = 0


class Seo(admin.TabularInline):
    model = Seo
    extra = 1
    max_num=1


class Departure(admin.TabularInline):
    model = Departure
    extra = 1

admin.site.register(Include)
admin.site.register(Execlude)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title', ]
    }
    list_display = ('title', 'image_preview', 'is_active', 'created_at')
    list_editable = ('is_active',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title', ]
    }
    list_display = ('title', 'thumbnail',
                    'destination', 'is_active', 'ordering')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    thumbnail.short_description = 'Preview'
    # list_editable = ('status', 'ordering')


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title', ]
    }
    list_display = ('title', 'thumbnail', 'is_active')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    thumbnail.short_description = 'Preview'


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    save_as = True

    prepopulated_fields = {
        'slug': ['title', ]
    }
    list_display = ['title', 'thumbnail', 'destination',
                    'activity', 'is_featured', 'is_active']
    list_editable = ['is_featured',]
    search_fields = ['title__istartswith',]
    list_filter = ['destination', 'activity']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    inlines = (Itinerary, Gallery, Faq, Seo, Departure)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    thumbnail.short_description = 'Preview'


# @admin.register(TourBooking)
# class TourBookingAdmin(admin.ModelAdmin):

#     list_display = ['package', 'price', 'departure_date',
#                     'full_name', 'email', 'contact_number', 'nationality']


admin.site.register(CustomizeTrip)

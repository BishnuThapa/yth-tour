from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
import os
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Convert
# Create your models here.


class Destination(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='destinations',
                              help_text='1920*1280 px')
    description = CKEditor5Field(config_name='extends')
    ordering = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destination'

    # Resized JPEG (fallback)
    image_optimized = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200)],
        format='JPEG',
        options={'quality': 80}
    )

    # WebP optimized version
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200), Convert('WEBP')],
        format='WEBP',
        options={'quality': 80}
    )


class Activity(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='activities')
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name='activities')
    description = CKEditor5Field(config_name='extends', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    ordering = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    # Resized JPEG (fallback)
    image_optimized = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200)],
        format='JPEG',
        options={'quality': 80}
    )

    # WebP optimized version
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200), Convert('WEBP')],
        format='WEBP',
        options={'quality': 80}
    )


class Style(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    icon = models.ImageField(upload_to='travelstyle', null=True, blank=True)
    image = models.ImageField(upload_to='travelstyle')
    # destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    description = CKEditor5Field(config_name='extends', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Travel Style'
        verbose_name_plural = 'Travel Styles'

    # Resized JPEG (fallback)
    image_optimized = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200)],
        format='JPEG',
        options={'quality': 80}
    )

    # WebP optimized version
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200), Convert('WEBP')],
        format='WEBP',
        options={'quality': 80}
    )


class Include(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Includes"
        verbose_name_plural = "Includes"


class Execlude(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Exclude"
        verbose_name_plural = "Excludes"



class Tour(models.Model):
    DIFFICULTY_CHOICES = (
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High')
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='tour')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='tours')
    duration = models.IntegerField(null=True, blank=True)
    difficulty = models.CharField(
        choices=DIFFICULTY_CHOICES, max_length=50, default='Low', null=True, blank=True)
    max_altitude = models.CharField(max_length=100, null=True, blank=True)
    best_season = models.CharField(max_length=100, null=True, blank=True)
    accomodation = models.CharField(max_length=100, null=True, blank=True)
    food = models.CharField(max_length=100, null=True, blank=True)
    transpotation = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    starting_date = models.DateField(null=True, blank=True)
    group_size = models.CharField(max_length=100, null=True, blank=True)
    regular_price = models.IntegerField(null=True, blank=True)
    sell_price = models.IntegerField(null=True, blank=True)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, null=True, blank=True)
    style = models.ManyToManyField(Style, null=True, blank=True)

    overview = CKEditor5Field(config_name='extends')
    includes = models.ManyToManyField(Include, null=True, blank=True)
    excludes = models.ManyToManyField(Execlude,null=True, blank=True)
    route_map = models.ImageField(upload_to='tour/map', null=True, blank=True)
    promotional_video = models.URLField(null=True, blank=True, help_text="Enter YouTube video URL")

    # itinerary = CKEditor5Field(config_name='extends',null=True, blank=True)
    gear_check_list = CKEditor5Field(config_name='extends',null=True, blank=True)
    
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def get_percentage(self):
        new_price = ((self.regular_price-self.sell_price)*100) / \
            self.regular_price
        return new_price
    
     # ✅ Convert YouTube link to embeddable iframe URL
    def get_embed_url(self):
        if self.promotional_video:
            if "watch?v=" in self.promotional_video:
                return self.promotional_video.replace("watch?v=", "embed/")
            elif "youtu.be/" in self.promotional_video:
                return self.promotional_video.replace("youtu.be/", "www.youtube.com/embed/")
            return self.promotional_video
        return None
        
     # Resized JPEG (fallback)
    image_optimized = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200)],
        format='JPEG',
        options={'quality': 80}
    )

    # WebP optimized version
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200), Convert('WEBP')],
        format='WEBP',
        options={'quality': 80}
    )


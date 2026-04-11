from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
import os
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Convert


class Team(models.Model):
    image = models.ImageField(upload_to='team', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    description = CKEditor5Field(config_name='extends')
    ordering = models.IntegerField()

    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
    
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

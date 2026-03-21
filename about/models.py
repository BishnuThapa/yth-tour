from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
import os
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Convert


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='aboutus',  null=True, blank=True)
    short_description = models.TextField()
    description = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

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


class WhyUs(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Why to choose Us'
        verbose_name_plural = 'Why to choose Us'

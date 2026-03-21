from imagekit.processors import ResizeToFit, Convert
from imagekit.models import ImageSpecField
from PIL import Image
import os
from django.conf import settings
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Service(models.Model):
    image = models.ImageField(upload_to='service')
    heading = models.CharField(max_length=255, null=True, blank=True)
    sub_heading = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    ordering = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

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

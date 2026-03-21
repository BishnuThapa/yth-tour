from django.db import models
from PIL import Image
from django.conf import settings
import os
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Convert

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activities')
    is_active = models.BooleanField(default=True)
    ordering = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Legal Document'
        verbose_name_plural = 'Legal Documents'
        
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

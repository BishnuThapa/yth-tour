from django.shortcuts import render
from .models import DayTour, Gallery
# Create your views here.

def daytour(request):
    daytours = DayTour.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'daytours': daytours,
    }
    return render(request, 'daytour.html', context)

def daytour_detail(request, slug):
    daytour = DayTour.objects.filter(slug=slug, is_active=True).first()
    gallery_images = Gallery.objects.filter(tour=daytour)
    related_daytours = DayTour.objects.filter(is_active=True).exclude(id=daytour.id)[:3]
    context = {
        'daytour': daytour,
        'gallery_images': gallery_images,
        'related_daytours': related_daytours,
    }
    return render(request, 'daytour_detail.html', context)
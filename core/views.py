from django.shortcuts import render, get_object_or_404
from slider.models import Slider
from blog.models import Blog
from about.models import AboutUs, WhyUs
from legaldocument.models import Document
from .models import Destination, Tour,Itinerary,Faq,Style
from django.db.models import Count, Q
from team.models import Team
# Create your views here.


def index(request):
    banner = Slider.objects.first()
    about = AboutUs.objects.first()
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')[:3]
    all_destinations = Destination.objects.filter(is_active=True)
    featured_tours=Tour.objects.filter(is_active=True, is_featured=True)[:6]
    styles=Style.objects.all()
    context = {
        'banner': banner,
        'all_destinations': all_destinations,
        'about': about,
        'blogs': blogs,
        'styles': styles,
        'featured_tours': featured_tours,

    }
    return render(request, 'index.html', context)


def about(request):
    about = AboutUs.objects.first()
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')[:3]

    context = {
        'about': about,
        'blogs': blogs,

    }
    return render(request, 'about.html', context)


def whyus(request):
    whyus = WhyUs.objects.first()
    context = {
        'whyus': whyus,

    }
    return render(request, 'why-us.html', context)


def legal(request):
    legaldocs = Document.objects.all()

    context = {
        'legaldocs': legaldocs,

    }
    return render(request, 'legal-documents.html', context)


def destination(request):
    # destinations = Destination.objects.all()
    destinations = Destination.objects.annotate(
        tour_count=Count('tours')).order_by('id')
    context = {
        'destinations': destinations,
    }
    return render(request, 'destination.html', context)


def destination_detail(request, slug):
    destination = get_object_or_404(
        Destination.objects.prefetch_related('tours'),
        slug=slug
    )

    tours = destination.tours.filter(is_active=True)
    context = {
        'destination': destination,
        'tours': tours,

    }
    return render(request, 'destination-detail.html', context)


def trip(request, slug):
    tour = get_object_or_404(
        Tour.objects.prefetch_related('gallery_set'),
        slug=slug
    )
    itineraries = Itinerary.objects.filter(tour=tour).order_by('day')
    faqs = Faq.objects.filter(tour=tour)
    # seo = Seo.objects.first()
    # featured_tours = Tour.objects.all().filter(is_featured=True)[:4]
    related_tours = Tour.objects.filter(
        destination=tour.destination
    ).exclude(
        id=tour.id
    ).order_by('-created_at')[:3]
    teams=Team.objects.all().order_by('ordering')

    context = {
        'tour': tour,
        'itineraries': itineraries,
        'faqs': faqs,
        'related_tours': related_tours,
        'teams': teams,

        # 'seo': seo,
        # 'featured_tours': featured_tours
    }

    return render(request, 'trip.html', context)




def contact(request):

    return render(request, 'contact.html')

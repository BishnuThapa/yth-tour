from django.shortcuts import render,get_object_or_404
from slider.models import Slider
from blog.models import Blog
from about.models import AboutUs,WhyUs
from legaldocument.models import Document
from .models import Destination
from django.db.models import Count, Q
# Create your views here.


def index(request):
    banner = Slider.objects.first()
    context={
        'banner': banner,
    }
    return render(request, 'index.html',context)

def about(request):
    about = AboutUs.objects.first()
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')[:3]

    context = {
        'about': about,
        'blogs': blogs,

    }
    return render(request, 'about.html',context)


def whyus(request):
    whyus = WhyUs.objects.first()
    context = {
        'whyus': whyus,

    }
    return render(request, 'why-us.html',context)


def legal(request):
    legaldocs = Document.objects.all()

    context = {
        'legaldocs': legaldocs,

    }
    return render(request, 'legal-documents.html',context)

       
def destination(request):
    # destinations = Destination.objects.all()
    destinations = Destination.objects.annotate(
        tour_count=Count('tours')).order_by('id')
    context = {
        'destinations': destinations,
    }
    return render(request, 'destination.html', context)


def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    # tours = Tour.objects.filter(
    #     destination__title=destination)
    context = {
        'destination': destination,
        # 'tours': tours,

        # 'categories': categories,
        # 'related_products': related_products
    }
    return render(request, 'destination-detail.html', context)



def contact(request):
   
    return render(request, 'contact.html')
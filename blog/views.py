from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import *
# Create your views here.


def blog(request):
    blog_list = Blog.objects.filter(is_active=True).order_by('-created_at')

    paginator = Paginator(blog_list, 3)  # 👈 3 blogs per page
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    related_blogs = Blog.objects.filter(
        is_active=True
    ).exclude(id=blog.id).order_by('-created_at')[:3]
    context = {
        'blog': blog,
        'related_blogs': related_blogs,
    }

    return render(request, 'blog_detail.html',context)

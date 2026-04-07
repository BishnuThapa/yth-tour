from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about,name='about'),
    path('why-to-choose-us/', views.whyus, name='whyus'),
    path('legal-documents/', views.legal, name='legal'),
    path('team/', include('team.urls')),

    path('destination/', views.destination, name='destination'),
    path('destination/<slug:slug>/', views.destination_detail, name='destination-detail'),
    
    path('page/', include('page.urls')),
    path('day-tour/', include('daytour.urls')),
    path('contact-us', views.contact, name='contact'),
]

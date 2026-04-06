from django.urls import path
from . import views

# app_name = 'blog'
urlpatterns = [
    path('', views.daytour, name='daytour'),
    path('<slug:slug>/', views.daytour_detail, name='daytour_detail'),
]

from django.shortcuts import render
from .models import *
# Create your views here.


def team(request):
    # banner = Banner.objects.first()
    # teams=Team.objects.all()
    # context={
    #     # 'banner':banner,
    #     'teams':teams
    # }
    return render(request,'team.html')
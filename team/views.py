from django.shortcuts import render
from .models import *
# Create your views here.


def team(request):
    
    teams=Team.objects.all()
    context={
       
        'teams':teams
    }
    return render(request,'team.html',context)

def team_detail(request,slug):
    team=Team.objects.get(slug=slug)
    context={
        'team':team
    }
    return render(request,'team_detail.html',context)
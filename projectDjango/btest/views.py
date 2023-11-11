from django.http import HttpResponse
from .models import Chanells

from django.shortcuts import render
from .models import Chanells, TVShows, Type

def index(request):
    bbs = Chanells.objects.all()
    return render(request, "btest/index.html", {'bbs': bbs})

def tv_shows_list(request):
    tv_shows = TVShows.objects.all()
    return render(request, "btest/index.html", {'tv_shows': tv_shows})

def type_shows_list(request):
    type_shows = Type.objects.all()
    return render(request, 'btest/index.html', {'type_shows': type_shows})

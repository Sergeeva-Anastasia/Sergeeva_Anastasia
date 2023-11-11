from django.http import HttpResponse
from django.shortcuts import render
from .models import Chanells, TVShows, Type

def index(request):
    bbs = Chanells.objects.all()
    tv_shows = TVShows.objects.all()
    type_shows = Type.objects.all()
    data = {'bbs': bbs, 'tv_shows': tv_shows, 'type_shows': type_shows}
    return HttpResponse(render(request, "btest/index.html", data))

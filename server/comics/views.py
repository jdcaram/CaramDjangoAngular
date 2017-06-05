from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from server.comics.models import ComicUniverse, Hero
from server.comics.serializers import ComicUniverseSerializer, HeroSerializer


class ComicUniverseViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing ComicUniverse objects """
    queryset = ComicUniverse.objects.all()
    serializer_class = ComicUniverseSerializer


class HeroViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Hero objects """
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


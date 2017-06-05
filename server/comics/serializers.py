from rest_framework import serializers
from server.comics.models import ComicUniverse, Hero


class ComicUniverseSerializer(serializers.ModelSerializer):
    """ Serializer to represent the ComicUniverse model """
    class Meta:
        model = ComicUniverse
        fields = ("company_name", "universe_name")


class HeroSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Hero model """
    class Meta:
        model = Hero
        fields = ("id", "name")


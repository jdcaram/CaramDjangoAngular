from django.contrib import admin

from server.comics.models import ComicUniverse, Hero


@admin.register(ComicUniverse)
class ComicUniverseAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'universe_name',
    ]
    list_filter = []
    search_fields = ['number', 'first_name', ]


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    list_filter = []
    search_fields = ['name', ]

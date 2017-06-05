from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class ComicUniverse(models.Model):
    """ Comic Company."""
    company_name = models.CharField(max_length=200)
    universe_name = models.CharField(max_length=100)

    def __str__(self):
        return "{0} ({1})".format(self.company_name, self.pk)


class Hero(models.Model):
    name = models.CharField(max_length=100)
    secret_identity = models.CharField(max_length=200, blank=True)
    comic_universe = models.ForeignKey(ComicUniverse, null=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.pk)

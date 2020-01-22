from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    capital = models.CharField(max_length=100)
    population = models.IntegerField()
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.country)

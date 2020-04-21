from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40)


class Feature(models.Model):
    name = models.CharField(max_length=40)


class Event(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )
    feature = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE
    )

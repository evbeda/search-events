from django.db import models

from search_events_app.models.country import Country
from search_events_app.mixins.get_context_mixin import GetContextMixin


# Create your models here.
class City(models.Model, GetContextMixin):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Cities'

    @classmethod
    def get_context(cls):
        cities = City.objects.all()

        return {
            'cities': [
                {
                    'code': city.code,
                    'name': city.name,
                    'country': city.country,
                } for city in cities
            ]
        }

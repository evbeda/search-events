from django.db import models

from search_events_app.mixins.get_context_mixin import GetContextMixin
from search_events_app.models.city import City


# Create your models here.
class Country(models.Model, GetContextMixin):
    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(max_length=2)
    eventbrite_id = models.CharField(max_length=30)

    def __init__(
        self,
        id=None,
        label=None,
        code=None,
        eventbrite_id=None,
        **kwargs
    ):
        super().__init__(
            id=id,
            name=label,
            alpha_2_code=code,
            eventbrite_id=eventbrite_id
        )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Countries'

    @classmethod
    def get_context(cls):
        countries = Country.objects.all()

        return {
            'countries': [
                {
                    'code': country.alpha_2_code,
                    'name': country.name,
                    'cities': cls.get_cities(country.alpha_2_code),
                } for country in countries
            ]
        }

    @classmethod
    def get_cities(cls, code):
        cities = City.objects.filter(country=code)
        return [{'code': city.code, 'name': city.name} for city in cities]

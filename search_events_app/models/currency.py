from django.db import models

from search_events_app.mixins.get_context_mixin import GetContextMixin


class Currency(models.Model, GetContextMixin):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Currencies'

    @classmethod
    def get_context(cls):
        currencies = Currency.objects.all()

        return {
            'currencies': [
                {
                    'code': currency.code,
                    'name': currency.name,
                } for currency in currencies
            ]
        }

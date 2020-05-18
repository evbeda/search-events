from django.db import models

from search_events_app.mixins.get_context_mixin import GetContextMixin


class Feature(models.Model, GetContextMixin):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Features'

    @classmethod
    def get_context(cls):

        features = Feature.objects.all()

        return {
            'features': [
                {
                    'code': feature.code,
                    'name': feature.name,
                } for feature in features
            ]
        }

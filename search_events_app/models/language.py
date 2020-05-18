from django.db import models

from search_events_app.mixins.get_context_mixin import GetContextMixin


class Language(models.Model, GetContextMixin):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'
    
    @classmethod
    def get_context(cls):
        languages = cls.objects.order_by('name')

        return {
            'languages': [
                {
                    'code': language.code,
                    'name': language.name
                } for language in languages
            ]
        }

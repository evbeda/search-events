from django.db import models

from search_events_app.mixins.get_context_mixin import GetContextMixin


class Format(models.Model):

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_context(cls):

        formats = Format.objects.all()

        return {
            'formats': [
                {
                    'code': format_.code,
                    'name': format_.name,
                } for format_ in formats
            ]
        }

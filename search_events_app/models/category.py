from django.db import models

from search_events_app.mixins.get_context_mixin import GetContextMixin


class Category(models.Model, GetContextMixin):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Categories'

    @classmethod
    def get_context(cls):

        categories = Category.objects.all()

        return {
            'categories': [
                {
                    'name': category.name,
                    'code': category.code,
                } for category in categories
            ]
        }

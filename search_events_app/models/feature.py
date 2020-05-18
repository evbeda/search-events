from django.db import models


class Feature(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Features'

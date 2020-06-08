from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Cities'

from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    flag = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"
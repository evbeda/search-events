from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    flag = models.URLField()

    def __init__(self, name=None, alpha2Code=None, alpha3Code=None, flag=None, **kwargs):
        if name and alpha2Code and alpha3Code and flag:
            super().__init__(name=name, alpha_2_code=alpha2Code, alpha_3_code=alpha3Code, flag=flag)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"

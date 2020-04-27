from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    flag = models.URLField()

    def __init__(
        self,
        id=None,
        name=None,
        alpha2Code=None,
        alpha3Code=None,
        flag=None,
        **kwargs
    ):
        super().__init__(
            id=id,
            name=name,
            alpha_2_code=alpha2Code,
            alpha_3_code=alpha3Code,
            flag=flag
        )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"

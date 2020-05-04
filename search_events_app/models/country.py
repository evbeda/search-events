from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(max_length=2)
    eventbrite_id = models.CharField(max_length=30)

    def __init__(
        self,
        id=None,
        label=None,
        code=None,
        eventbrite_id=None,
        **kwargs
    ):
        super().__init__(
            id=id,
            name=label,
            alpha_2_code=code,
            eventbrite_id=eventbrite_id
        )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"

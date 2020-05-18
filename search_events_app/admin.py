from django.contrib import admin

from .models.country import Country
from .models.feature import Feature
from .models.language import Language


# Register your models here.
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Feature)

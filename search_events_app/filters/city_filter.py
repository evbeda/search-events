from django.core.exceptions import ObjectDoesNotExist

from search_events_app.models import (
    City,
    Country,
)
from search_events_app.filters.filter import Filter


class CityFilter(Filter):

    def apply_filter(self, request):
        country_name = request.GET.get('country', '')
        city_name = request.GET.get('city', '')
        new_filter = None
        if city_name:
            try:
                country = Country.objects.get(name=country_name)
                new_filter = City.objects.get(name=city_name, country=country.alpha_2_code )
            except ObjectDoesNotExist:
                new_filter = None
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            if self.value.code:
                return f" AND dw_event.event_venue_state = '{self.value.code}' "
            return f" AND (dw_event.event_venue_state = '{self.value.name}' OR dw_event.event_venue_city = '{self.value.name}')"
        return ''

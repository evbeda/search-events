from django.core.exceptions import ObjectDoesNotExist

from search_events_app.services.filters.filter import Filter
from search_events_app.models.country import Country


class CountryFilter(Filter):

    def apply_filter(self, request):
        alpha_2_code = request.GET.get('country') if request.GET.get('country') else None
        new_filter = None
        if alpha_2_code:
            try:
                new_filter = Country.objects.get(alpha_2_code=alpha_2_code)
            except ObjectDoesNotExist:
                new_filter = None
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_key(self):
        return "country"

    def get_value(self):
        if self.value:
            return self.value.name

    def get_type(self):
        return "search"

    def get_request_value(self):
        if self.value:
            return {
                'places_within': [self.value.eventbrite_id]
            }

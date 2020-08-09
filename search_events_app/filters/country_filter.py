from django.core.exceptions import ObjectDoesNotExist

from search_events_app.models import Country
from search_events_app.filters.filter import Filter


class CountryFilter(Filter):

    def apply_filter(self, request):
        country_name = request.GET.get('country')
        new_filter = None
        if country_name:
            try:
                new_filter = Country.objects.get(name=country_name)
            except ObjectDoesNotExist:
                pass
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_where_query(self):
        if self.value:
            return f"AND country_desc='{self.value.alpha_2_code}'"
        return ''

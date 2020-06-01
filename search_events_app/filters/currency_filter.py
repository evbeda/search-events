from django.core.exceptions import ObjectDoesNotExist

from search_events_app.filters.filter import Filter
from search_events_app.models.currency import Currency


class CurrencyFilter(Filter):
    def apply_filter(self, request):
        currency_code = request.GET.get('currency', '')
        new_filter = None
        if currency_code:
            try:
                new_filter = Currency.objects.get(code=currency_code)
            except ObjectDoesNotExist:
                new_filter = None
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return f" AND dw_event.event_currency = '{self.value.code}' "
        return ''

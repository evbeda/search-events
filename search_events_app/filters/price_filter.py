from search_events_app.filters.filter import Filter


class PriceFilter(Filter):

    def apply_filter(self, request):
        price = request.GET.get('price')
        new_filter = None
        if price:
            new_filter = f'{price} event'

        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return f" AND dw_event.event_paid_type = '{self.value}'"
        return ''

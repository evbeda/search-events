from search_events_app.filters.filter import Filter


class EventNameFilter(Filter):
    def apply_filter(self, request):
        event_name = request.GET.get('event_name', '')
        new_filter = None
        if event_name:
            new_filter = event_name
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return f"AND LOWER(dw_event.event_title) LIKE '%{self.value.lower().strip()}%'"
        return ''

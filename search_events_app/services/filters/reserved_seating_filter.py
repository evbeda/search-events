from search_events_app.services.filters.filter import Filter


class ReservedSeatingFilter(Filter):

    def apply_filter(self, feature_codes):
        code = 'RS'
        new_filter = code in feature_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ''

    def get_where_query(self):
        if self.value:
            return f" AND dw_event.is_reserved_seating = 'Y' "
        return ''

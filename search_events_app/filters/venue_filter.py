from search_events_app.filters.filter import Filter


class VenueFilter(Filter):

    def apply_filter(self, request):
        venue = request.GET.get('venue', '').strip()
        new_filter = None
        if venue:
            new_filter = venue

        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_where_query(self):
        if self.value:
            return 'AND (' \
                    "LOWER(CONCAT(venue_desc, ', ', event_venue_city, ', ', " \
                    "event_venue_state, ' ', event_venue_postal_code)) " \
                    f"LIKE '%{self.value.lower()}%'" \
                ')'
        return ''

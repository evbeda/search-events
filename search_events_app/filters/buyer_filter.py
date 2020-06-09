from django.core.exceptions import ObjectDoesNotExist

from search_events_app.filters.filter import Filter


class BuyerFilter(Filter):

    def apply_filter(self, request):
        buyer_name = request.GET.get('buyer', '').strip()
        new_filter = None
        if buyer_name:
            new_filter = buyer_name
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        if self.value:
            return [
                "INNER JOIN ("\
                "SELECT event, CONCAT(first_name, ' ', last_name) AS attendee_name "\
                "FROM hive.eb.attendees "\
                f"WHERE LOWER(CONCAT(first_name, ' ', last_name)) LIKE '%{self.value.lower()}%'"\
            ") AS at ON at.event = dw_event.event_id"
            ]
        return ['']

    def get_where_query(self):
        return ''

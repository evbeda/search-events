from search_events_app.filters.filter import Filter


class LastFourFilter(Filter):

    def apply_filter(self, request):
        last_four = request.GET.get('card', '')
        new_filter = None
        if last_four:
            new_filter = last_four

        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        if self.value:
            return [
                'INNER JOIN ('
                    'SELECT o.event, o.id '
                    'FROM hive.eb.orders o '
                    'INNER JOIN ('
                        'SELECT order_id '
                        'FROM hive.eb.orders_payment '
                        f"WHERE last_four = '{self.value}'"
                        ') AS op ON op.order_id = o.id'
                ') AS o on o.event = dw_event.event_id'
            ]
        return ['']

    def get_where_query(self):
        return ''

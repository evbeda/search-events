from search_events_app.filters.filter import Filter


class StartDateFilter(Filter):

    def apply_filter(self, request):
        full_date_range = request.GET.get('datefilter')
        new_filter = None
        if full_date_range:
            date_array = full_date_range.split(' to ')
            new_filter = {
                'start': date_array[0],
                'end': date_array[len(date_array)-1]
            }
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return 'AND CAST(CAST(event_start_date AS TIMESTAMP) AS DATE) ' \
                        f"BETWEEN CAST('{self.value['start']}' AS DATE) " \
                        f"AND CAST('{self.value['end']}' AS DATE)"
        return ''

from search_events_app.services.filters.filter import Filter


class CustomQuestionFilter(Filter):
    code = 'CQ'

    def apply_filter(self, feature_codes):
        new_filter = self.code in feature_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        if self.value:
            query = ['INNER JOIN eb.questions q ON q.asset = dw_event.event_id']
            return query
        return ['']

    def get_where_query(self):
        return ''

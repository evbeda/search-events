from search_events_app.services.filters.filter import Filter
from search_events_app.utils.feature_codes import FeatureCodes


class CustomQuestionFilter(Filter):
    def apply_filter(self, feature_codes):
        new_filter = FeatureCodes.custom_question in feature_codes
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

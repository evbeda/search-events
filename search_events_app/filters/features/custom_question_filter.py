from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class CustomQuestionFilter(Filter):
    def apply_filter(self, feature_codes):
        super().apply_filter(FeatureCodes.custom_question, feature_codes)

    def get_join_query(self):
        if self.value:
            return ['INNER JOIN eb.questions q ON q.asset = dw_event.event_id']
        return ['']

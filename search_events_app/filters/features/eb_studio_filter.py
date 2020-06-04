from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class EBStudioFilter(Filter):
    def apply_filter(self, features_codes):
        new_filter = FeatureCodes.eventbrite_studio in features_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return " AND es.domain IS NOT NULL"
        return ''


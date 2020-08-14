from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class EBStudioFilter(Filter):
    def apply_filter(self, feature_codes):
        super().apply_filter(FeatureCodes.eventbrite_studio, feature_codes)

    def get_where_query(self):
        if self.value:
            return 'AND es.domain IS NOT NULL'
        return ''


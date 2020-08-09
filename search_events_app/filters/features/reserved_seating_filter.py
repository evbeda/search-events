from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class ReservedSeatingFilter(Filter):
    def apply_filter(self, feature_codes):
        super().apply_filter(FeatureCodes.reserved_seating, feature_codes)

    def get_where_query(self):
        if self.value:
            return f"AND dw_event.is_reserved_seating = 'Y'"
        return ''

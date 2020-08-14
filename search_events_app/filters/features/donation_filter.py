from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class DonationFilter(Filter):
    def apply_filter(self, feature_codes):
        super().apply_filter(FeatureCodes.donation, feature_codes)

    def get_where_query(self):
        if self.value:
            return 'AND ts.donation > 0'
        return ''

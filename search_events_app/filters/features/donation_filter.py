from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class DonationFilter(Filter):
    def apply_filter(self, feature_codes):
        new_filter = FeatureCodes.donation in feature_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return ' AND ts.donation > 0 '
        return ''

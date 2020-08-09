from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class AddOnsFilter(Filter):
    def apply_filter(self, feature_codes):
        super().apply_filter(FeatureCodes.add_ons, feature_codes)

    def get_where_query(self):
        if self.value:
            return "AND f.trx_type = 'add_on_ticket_purchase'"
        return ''

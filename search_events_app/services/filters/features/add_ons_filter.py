from search_events_app.services.filters.filter import Filter
from search_events_app.utils.feature_codes import FeatureCodes


class AddOnsFilter(Filter):
    def apply_filter(self, features_codes):
        new_filter = FeatureCodes.add_ons in features_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter     

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return " AND f.trx_type = 'add_on_ticket_purchase'"
        return ''

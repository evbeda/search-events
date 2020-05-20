from search_events_app.services.filters.filter import Filter
from search_events_app.utils.feature_codes import FeatureCodes


class WebsiteWidgetsFilter(Filter):
    def apply_filter(self, features_codes):
        new_filter = FeatureCodes.website_widgets in features_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        if self.value:
            join_ticket = "INNER JOIN dw.f_ticket_merchandise_purchase f ON f.event_id = dw_event.event_id"
            join_affiliate = "INNER JOIN dw.dim_affiliate_code_group dacg ON dacg.affiliate_code = f.q_order_affiliate_code"
            join_query = [join_ticket, join_affiliate]
            return join_query
        return ['']

    def get_where_query(self):
        if self.value:
            return " AND dacg.affiliate_group_2 = 'Website Widgets'"
        return ''
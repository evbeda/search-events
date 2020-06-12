from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class WebsiteWidgetsFilter(Filter):
    def apply_filter(self, features_codes):
        new_filter = FeatureCodes.website_widgets in features_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        if self.value:
            return [
                'INNER JOIN ('
                    'SELECT affiliate_code, affiliate_group_2 '
                    'FROM hive.dw.dim_affiliate_code_group'
                ') AS dacg ON dacg.affiliate_code = f.q_order_affiliate_code'
                ]
        return ['']

    def get_where_query(self):
        if self.value:
            return "AND dacg.affiliate_group_2 = 'Website Widgets'"
        return ''

from search_events_app.services.filters.filter import Filter


class FeatureFilterManager(Filter):
    def __init__(self):
        super().__init__()
        self.value = []

    def apply_filter(self, request):
        features_codes = request.GET.get('features').split('-')
        new_filter = None
        if features_codes:
            for latest_filter in self.value:
                latest_filter.apply_filter(features_codes)
        self.has_changed = ([latest_filter for latest_filter in self.value if latest_filter.has_changed]) > 0      

    def get_key(self):
        return ''

    def get_value(self):
        return ''

    def get_type(self):
        return ''

    def get_request_value(self):
        return ''

    def get_join_query(self):
        join_query = ''
        for feature in self.value:
            join_query += feature.get_join_query()
        return join_query

    def get_where_query(self):
        where_query = ''
        for feature in self.value:
            where_query += feature.get_where_query()
        return where_query

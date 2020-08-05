from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class FacebookFilter(Filter):
    def apply_filter(self, features_codes):
        new_filter = FeatureCodes.facebook in features_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        if self.value:
            return [
                'INNER JOIN ('
                    'SELECT facebook_event_id, event_id '
                    'FROM hive.web.facebookpublishevent_action'
                ') AS fb ON dw_event.event_id = fb.event_id'
            ]
        return ['']


    def get_where_query(self):
        return ''

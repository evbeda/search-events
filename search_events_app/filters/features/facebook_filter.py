from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class FacebookFilter(Filter):
    def apply_filter(self, feature_codes):
        super().apply_filter(FeatureCodes.facebook, feature_codes)

    def get_select_query(self):
        if self.value:
            return ', fb.facebook_event_id'
        return ''

    def get_join_query(self):
        if self.value:
            return [
                'INNER JOIN ('
                    'SELECT facebook_event_id, event_id '
                    'FROM hive.web.facebookpublishevent_action'
                ') AS fb ON dw_event.event_id = fb.event_id'
            ]
        return ['']

    def get_group_query(self):
        if self.value:
            return ', fb.facebook_event_id'
        return ''

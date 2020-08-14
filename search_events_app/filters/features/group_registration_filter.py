from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class GroupRegistrationFilter(Filter):
    def apply_filter(self, feature_codes):
        super().apply_filter(FeatureCodes.group_registration, feature_codes) 

    def get_join_query(self):
        if self.value:
            return [
                'INNER JOIN ('
                'SELECT event_id '
                'FROM hive.eb.team'
                ') AS team ON dw_event.event_id = team.event_id'
            ]
        return ['']

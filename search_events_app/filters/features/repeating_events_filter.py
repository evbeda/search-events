from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class RepeatingEventsFilter(Filter):
	def apply_filter(self, feature_codes):
		super().apply_filter(FeatureCodes.repeating_events, feature_codes)

	def get_where_query(self):
		if self.value:
			return "AND dw_event.is_repeating_event = 'Y'"
		return ''

from search_events_app.services.filters.filter import Filter


class RepeatingEventsFilter(Filter):

	CODE = "RE"

	def apply_filter(self, feature_codes):
		new_filter = self.CODE in feature_codes
		self.has_changed = new_filter != self.value
		if self.has_changed:
			self.value = new_filter

	def get_join_query(self):
		return ''

	def get_where_query(self):
		if self.value:
			return " AND dw_event.is_repeating_event = 'Y'"
		return ''


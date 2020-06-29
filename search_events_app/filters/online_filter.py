from search_events_app.utils.online_parameters import OnlineParameters
from search_events_app.filters.filter import Filter


class OnlineFilter(Filter):

    def apply_filter(self, request):
        online = request.GET.get('online')
        new_filter = None
        if online:
            if online == 'on':
                new_filter = OnlineParameters.ONLINE
            elif online == 'off':
                new_filter = OnlineParameters.OFFLINE
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return f"AND dw_event.online_flag='{self.value.get('query_value')}' "\
                f"AND dw_event.country_desc IS {self.value.get('venue_value')} NULL"
        return ''

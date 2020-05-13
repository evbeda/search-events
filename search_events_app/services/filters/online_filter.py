from search_events_app.models.online_parameters import OnlineParameters
from search_events_app.services.filters.filter import Filter


class OnlineFilter(Filter):

    def apply_filter(self, request):
        online = request.GET.get('online') if request.GET.get('online') else None
        new_filter = None
        if online:
            if online == 'on':
                new_filter = 'Y'
            elif online == 'off':
                new_filter = 'N'
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_request_value(self):
        if self.value:
            dict_key = self.value.get('key')
            return {
                dict_key: True
            }

    def get_value(self):
        if self.value:
            return self.value

    def get_type(self):
        return 'search'

    def get_key(self):
        return 'online'

    def get_join_query(self):
        return ''

    def get_where_query(self):
        if self.value:
            return f" AND dw_event.online_flag='{self.value.get('query_value')}' "
        return ''

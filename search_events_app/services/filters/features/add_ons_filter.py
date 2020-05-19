from search_events_app.services.filters.filter import Filter


class AddOnsFilter(Filter):
    
    code = 'AO'

    def apply_filter(self, features_codes):
        new_filter = self.code in features_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter     

    def get_key(self):
        return ''

    def get_value(self):
        return ''

    def get_type(self):
        return ''

    def get_request_value(self):
        return ''

    def get_join_query(self):
        if self.value:
            return ' INNER JOIN dw.f_ticket_merchandise_purchase f ON f.event_id = dw_event.event_id'
        return ''

    def get_where_query(self):
        if self.value:
            return " AND f.trx_type = 'add_on_ticket_purchase'"
        return ''

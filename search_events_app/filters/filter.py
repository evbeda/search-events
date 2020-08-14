class Filter:

    def __init__(self):
        self.value = None
        self.has_changed = False

    def apply_filter(self, code, feature_codes):
        new_filter = code in feature_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_select_query(self):
        return ''

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        return ''

    def get_group_query(self):
        return ''

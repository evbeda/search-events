from abc import abstractmethod


class Filter:

    def __init__(self):
        self.value = None
        self.has_changed = False

    @abstractmethod
    def apply_filter(self, request):
        pass

    def get_select_query(self):
        return ''

    @abstractmethod
    def get_join_query(self):
        pass

    @abstractmethod
    def get_where_query(self):
        pass

    def get_group_query(self):
        return ''

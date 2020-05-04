from abc import abstractmethod


class Filter:

    def __init__(self):
        self.value = None
        self.has_changed = False

    @abstractmethod
    def apply_filter(self, request):
        pass

    @abstractmethod
    def get_key(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_type(self):
        pass
    
    @abstractmethod
    def get_request_value(self):
        pass
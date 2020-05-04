class StateManager:
    events = None

    @classmethod
    def set_events(cls, events):
        cls.events = events

    @classmethod
    def get_last_searched_events(cls):
        return cls.events

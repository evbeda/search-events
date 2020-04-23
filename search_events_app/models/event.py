class Event:

    def __init__(self, name, url, country=None, feature=None, **kwargs):
        self.name = name
        self.country = country
        self.url = url
        if not feature:
            self.feature = []
        else:
            self.feature = feature
        for key, value in kwargs.items():
            setattr(self, key, value)

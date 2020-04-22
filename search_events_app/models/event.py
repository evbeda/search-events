class Event:
    def __init__(self, name, url, country=None, feature=[]):
        self.name = name
        self.country = country
        self.feature = feature
        self.url = url

class Event:

    def __init__(
            self,
            name,
            url,
            country=None,
            feature=None,
            start_date=None,
            language=None,
            category=None,
            format_=None,
            organizer=None,
            **kwargs
    ):
        self.name = name
        self.country = country
        self.url = url
        self.start_date = start_date
        self.language = language
        self.category = category
        self.format = format_
        self.organizer = organizer
        if not feature:
            self.feature = []
        else:
            self.feature = feature

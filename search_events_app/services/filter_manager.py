from search_events_app.services.filters.country_filter import CountryFilter
from search_events_app.services.filters.online_filter import OnlineFilter


class FilterManager:
    latest_filters = [CountryFilter(), OnlineFilter()]

    @classmethod
    def apply_filters(cls, request):
        for latest_filter in cls.latest_filters:
            latest_filter.apply_filter(request)

    @classmethod
    def filter_has_changed(cls):
        return len([latest_filter for latest_filter in cls.latest_filters if latest_filter.has_changed]) > 0

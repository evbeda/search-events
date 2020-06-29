from search_events_app.dto import (
    DTOFilter,
    DTODBServiceFilter,
)
from search_events_app.filters import (
    BuyerFilter,
    CategoryFilter,
    CityFilter,
    CountryFilter,
    CurrencyFilter,
    EventNameFilter,
    FeatureFilterManager,
    FormatFilter,
    LanguageFilter,
    LastFourFilter,
    OnlineFilter,
    OrganizerFilter,
    PriceFilter,
    StartDateFilter,
    VenueFilter,
)


class FilterManager:
    latest_filters = [
        CountryFilter(),
        OnlineFilter(),
        LanguageFilter(),
        FormatFilter(),
        CategoryFilter(),
        PriceFilter(),
        CurrencyFilter(),
        CityFilter(),
        FeatureFilterManager(),
        EventNameFilter(),
        OrganizerFilter(),
        BuyerFilter(),
        VenueFilter(),
        StartDateFilter(),
        LastFourFilter()
    ]

    @classmethod
    def apply_filters(cls, request):
        for latest_filter in cls.latest_filters:
            latest_filter.apply_filter(request)

    @classmethod
    def filter_has_changed(cls):
        return len([latest_filter for latest_filter in cls.latest_filters if latest_filter.has_changed]) > 0

    @classmethod
    def get_list_dto_db_service_filter(cls):
        list_dto = []
        dict_dto = {}
        for filter_ in cls.latest_filters:
            dict_dto['join_query'] = filter_.get_join_query()
            dict_dto['where_query'] = filter_.get_where_query()
            list_dto.append(DTODBServiceFilter(**dict_dto))

        return list_dto

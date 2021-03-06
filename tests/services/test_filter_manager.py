from unittest.mock import (
    MagicMock,
    patch,
)

from django.test import TestCase

from search_events_app.dto.dto_db_service_filter import DTODBServiceFilter
from search_events_app.models import (
    Country,
    Language,
)
from search_events_app.services import FilterManager
from search_events_app.filters import (
    CountryFilter,
    FormatFilter,
    LanguageFilter,
    OnlineFilter,
    CategoryFilter,
)


class TestFilterManager(TestCase):

    @patch.object(CountryFilter, 'apply_filter')
    def test_filter_country(self, patch_apply):
        mock_request = MagicMock()
        mock_request.GET = MagicMock()
        mock_request.GET.get = MagicMock(return_value='AR')
        FilterManager.latest_filters = [CountryFilter(), CountryFilter()]
        FilterManager.apply_filters(mock_request)
        count = patch_apply.call_count
        self.assertEqual(count, 2)

    def test_filter_has_changed_true(self):
        FilterManager.latest_filters = [CountryFilter(), OnlineFilter(), LanguageFilter(), FormatFilter()]
        FilterManager.latest_filters[0].has_changed = True

        self.assertTrue(FilterManager.filter_has_changed())

    def test_filter_has_changed_false(self):
        FilterManager.latest_filters = [CountryFilter(), OnlineFilter(), LanguageFilter(), CategoryFilter()]

        self.assertFalse(FilterManager.filter_has_changed())

    def test_get_list_dto_db_service_filter(self):
        country_filter = CountryFilter()
        country_filter.value = Country(label='Argentina', code='AR', eventbrite_id='85632505')
        FilterManager.latest_filters = [country_filter]

        expected_where = "AND country_desc='AR'"
        expected_join = ['']
        result = FilterManager.get_list_dto_db_service_filter()

        self.assertEqual(result[0].where_query, expected_where)
        self.assertEqual(result[0].join_query, expected_join)
        self.assertIsInstance(result[0], DTODBServiceFilter)

    def test_get_list_dto_db_service_filter_by_filters(self):
        list_dto = [
            {'join_query': [''], 'where_query': "AND country_desc='AR'" }
        ]
   
        country_filter = CountryFilter()
        country_filter.value = Country(label='Argentina', code='AR', eventbrite_id='85632505')
        FilterManager.latest_filters = [country_filter]

        result = [
            {
                'join_query': dto.join_query,
                'where_query': dto.where_query
            }
            for dto in FilterManager.get_list_dto_db_service_filter()
        ]
        self.assertEqual(result, list_dto)

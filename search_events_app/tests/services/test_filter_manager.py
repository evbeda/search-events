from unittest.mock import (
    MagicMock,
    patch,
)

from django.test import TestCase

from search_events_app.dto.dto_filter import DTOFilter
from search_events_app.dto.dto_db_service_filter import DTODBServiceFilter
from search_events_app.models.country import Country
from search_events_app.models.language import Language
from search_events_app.services.filter_manager import FilterManager
from search_events_app.services.filters.country_filter import CountryFilter
from search_events_app.services.filters.language_filter import LanguageFilter
from search_events_app.services.filters.online_filter import OnlineFilter


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
        FilterManager.latest_filters = [CountryFilter(), OnlineFilter(), LanguageFilter()]
        FilterManager.latest_filters[0].has_changed = True

        self.assertTrue(FilterManager.filter_has_changed())

    def test_filter_has_changed_false(self):
        FilterManager.latest_filters = [CountryFilter(), OnlineFilter(), LanguageFilter()]

        self.assertFalse(FilterManager.filter_has_changed())

    def test_get_dto_filter_by_filters(self):
        country_filter = CountryFilter()
        country_filter.value = Country(label='Spain', code='ES')
        language_filter = LanguageFilter()
        language_filter.value = Language.objects.create(name='Spanish', code='es')
        FilterManager.latest_filters = [country_filter, OnlineFilter(), language_filter]

        result = FilterManager.get_dto_filter_by_filters()
        
        self.assertEqual(result.country, 'Spain')

    def test_get_list_dto_api_service_filter_by_filters(self):
        list_dto = [
            {'type': 'search', 'value': {'places_within': ['85632505']}},
            {'type': 'search', 'value': None},
            {'type': 'search', 'value': {'languages': ['es']}}
        ]
        
        country_filter = CountryFilter()
        country_filter.value = Country(label='Argentina', code='AR', eventbrite_id='85632505')
        language_filter = LanguageFilter()
        language_filter.value = Language.objects.create(name='Spanish', code='es')
        FilterManager.latest_filters = [country_filter, OnlineFilter(), language_filter]

        result = [
            {
                'type': dto.type,
                'value': dto.value
            }
            for dto in FilterManager.get_list_dto_api_service_filter_by_filters()
        ]
        self.assertEqual(result, list_dto)

        def test_get_list_dto_db_service_filter(self):
            country_filter = CountryFilter()
            country_filter.value = Country(label='Argentina', code='AR', eventbrite_id='85632505')
            FilterManager.latest_filters = [country_filter]

            expected_where = " AND country_desc='AR' "
            expected_join = ''
            result = FilterManager.get_list_dto_db_service_filter()

            self.assertEqual(result[0].where_query, expected_where)
            self.assertEqual(result[0].join_query, expected_join)
            self.assertIsInstance(result[0], DTODBServiceFilter)

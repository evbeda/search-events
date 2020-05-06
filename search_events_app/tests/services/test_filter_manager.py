from unittest.mock import (
    MagicMock,
    patch,
)

from django.test import TestCase

from search_events_app.services.filter_manager import FilterManager
from search_events_app.services.filters.country_filter import CountryFilter


class TestFilterManager(TestCase):

    @patch.object(
        CountryFilter,
        'apply_filter'
    )
    def test_filter_country(self, patch_apply):
        mock_request = MagicMock()
        mock_request.GET = MagicMock()
        mock_request.GET.get = MagicMock(return_value='AR')
        FilterManager.latest_filters = [CountryFilter(), CountryFilter()]
        FilterManager.apply_filters(mock_request)
        count = patch_apply.call_count
        self.assertEqual(count, 2)

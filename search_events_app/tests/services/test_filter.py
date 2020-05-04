from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.services.filters.country_filter import CountryFilter
from search_events_app.models.country import Country


class TestFilters(TestCase):

    def setUp(self):
        self.country = Country.objects.create(label='Argentina', code='AR', eventbrite_id="1234")
        self.country_filter = CountryFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_country_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='AR')

        self.country_filter.apply_filter(self.mock_request)

        self.assertEqual(self.country_filter.value.name, "Argentina")
        self.assertTrue(self.country_filter.has_changed)

    def test_not_apply_country_filter(self):
        self.country_filter.apply_filter(self.mock_request)

        self.assertFalse(self.country_filter.has_changed)
        self.assertIsNone(self.country_filter.value)

    def test_apply_country_filter_with_wrong_data(self):
        self.mock_request.GET.get = MagicMock(return_value='America')

        self.country_filter.apply_filter(self.mock_request)

        self.assertFalse(self.country_filter.has_changed)
        self.assertIsNone(self.country_filter.value)

    def test_apply_country_filter_same_value(self):
        self.country_filter.value = self.country
        self.mock_request.GET.get = MagicMock(return_value='AR')

        self.country_filter.apply_filter(self.mock_request)

        self.assertFalse(self.country_filter.has_changed)

    def test_country_filter_info(self):
        self.mock_request.GET.get = MagicMock(return_value='AR')

        self.country_filter.apply_filter(self.mock_request)

        self.assertEqual(self.country_filter.get_key(), "country")
        self.assertEqual(self.country_filter.get_value(), "Argentina")
        self.assertEqual(self.country_filter.get_type(), "search")
        self.assertEqual(self.country_filter.get_request_value(), {
            'place_within': "1234"
        })

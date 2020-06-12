from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.models import City
from search_events_app.filters import CityFilter


class TestCityFilter(TestCase):

    def setUp(self):
        self.city_filter = CityFilter()
        self.mock_request = MagicMock()

    def test_apply_city_filter(self):
        request_return = {
            'country': 'Argentina',
            'city': 'Mendoza',
        }
        self.mock_request.GET = request_return

        self.city_filter.apply_filter(self.mock_request)

        self.assertEqual(self.city_filter.value.name, 'Mendoza')
        self.assertEqual(self.city_filter.value.country, 'AR')
        self.assertTrue(self.city_filter.has_changed)

    def test_not_apply_city_filter(self):
        self.city_filter.apply_filter(self.mock_request)

        self.assertFalse(self.city_filter.has_changed)
        self.assertIsNone(self.city_filter.value)

    def test_apply_city_filter_with_wrong_data(self):
        request_return = {
            'country': 'Argentina',
            'city': 'Incorrect City',
        }
        self.mock_request.GET = request_return

        self.city_filter.apply_filter(self.mock_request)

        self.assertFalse(self.city_filter.has_changed)
        self.assertIsNone(self.city_filter.value)

    def test_apply_city_filter_same_value(self):
        request_return = {
            'country': 'United States',
            'city': 'Indiana',
            'code': 'IN',
        }
        self.mock_request.GET = request_return
        city = City.objects.get(name='Indiana', country='US', code='IN')
        self.city_filter.value = city
        self.mock_request.GET = request_return

        self.city_filter.apply_filter(self.mock_request)

        self.assertFalse(self.city_filter.has_changed)

    def test_city_filter_info_with_city_US_selected(self):

        self.city_filter.value = City(name='Indiana', country='US', code='IN')

        self.assertEqual(self.city_filter.get_join_query(), [''])
        self.assertEqual(self.city_filter.get_where_query(), "AND dw_event.event_venue_state = 'IN'")

    def test_city_filter_info_with_city_selected(self):

        self.city_filter.value = City(name='Mendoza', country='AR')

        self.assertEqual(self.city_filter.get_join_query(), [''])
        self.assertEqual(self.city_filter.get_where_query(), "AND (dw_event.event_venue_state = 'Mendoza' OR dw_event.event_venue_city = 'Mendoza')")

    def test_city_filter_info_without_city_selected(self):

        self.city_filter.value = None

        self.assertEqual(self.city_filter.get_join_query(), [''])
        self.assertEqual(self.city_filter.get_where_query(), '')

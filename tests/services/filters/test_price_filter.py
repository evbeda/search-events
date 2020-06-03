from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.utils import OnlineParameters
from search_events_app.filters import PriceFilter


class TestPriceFilter(TestCase):

    def setUp(self):
        self.price_filter = PriceFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_price_filter_free_events(self):
        self.mock_request.GET.get = MagicMock(return_value='free')

        self.price_filter.apply_filter(self.mock_request)
        self.assertEqual(self.price_filter.value, 'free event')
        self.assertTrue(self.price_filter.has_changed)

    def test_apply_price_filter_paid_events(self):
        self.mock_request.GET.get = MagicMock(return_value='paid')

        self.price_filter.apply_filter(self.mock_request)
        self.assertEqual(self.price_filter.value, 'paid event')
        self.assertTrue(self.price_filter.has_changed)

    def test_apply_price_filter_all_events(self):
        self.mock_request.GET.get = MagicMock(return_value='')

        self.price_filter.apply_filter(self.mock_request)
        self.assertEqual(self.price_filter.value, None)
        self.assertFalse(self.price_filter.has_changed)

    def test_apply_price_filter_same_value(self):
        self.price_filter.value = 'paid event'
        self.mock_request.GET.get = MagicMock(return_value='paid')

        self.price_filter.apply_filter(self.mock_request)

        self.assertFalse(self.price_filter.has_changed)

    def test_price_filter_info_with_option_selected(self):
        self.price_filter.value = 'free event'

        expected_where_query = " AND dw_event.event_paid_type = 'free event'"
        
        self.assertEqual(self.price_filter.get_join_query(), [''])
        self.assertEqual(self.price_filter.get_where_query(), expected_where_query)
    
    def test_price_filter_info_with_option_selected_paid_event(self):
        self.price_filter.value = 'paid event'

        expected_where_query = " AND (dw_event.event_paid_type = 'paid event' OR dw_event.event_paid_type = 'mixed event') "
        
        self.assertEqual(self.price_filter.get_join_query(), [''])
        self.assertEqual(self.price_filter.get_where_query(), expected_where_query)
    
    def test_price_filter_info_without_option_selected(self):
        self.price_filter.value = None

        self.assertEqual(self.price_filter.get_join_query(), [''])
        self.assertEqual(self.price_filter.get_where_query(), '')

from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.utils import OnlineParameters
from search_events_app.filters import OnlineFilter


class TestOnlineFilter(TestCase):

    def setUp(self):
        self.online_filter = OnlineFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_online_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='on')

        self.online_filter.apply_filter(self.mock_request)
        self.assertEqual(self.online_filter.value, OnlineParameters.ONLINE)
        self.assertTrue(self.online_filter.has_changed)

    def test_apply_offline_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='off')

        self.online_filter.apply_filter(self.mock_request)
        self.assertEqual(self.online_filter.value, OnlineParameters.OFFLINE)
        self.assertTrue(self.online_filter.has_changed)

    def test_not_online_apply_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='both')

        result = self.online_filter.apply_filter(self.mock_request)

        self.assertIsNone(result)
        self.assertFalse(self.online_filter.has_changed)

    def test_apply_online_filter_with_wrong_url_parameter(self):
        self.mock_request.GET.get = MagicMock(return_value='aras')

        result = self.online_filter.apply_filter(self.mock_request)

        self.assertIsNone(result)
        self.assertFalse(self.online_filter.has_changed)

    def test_apply_online_filter_same_value(self):
        self.online_filter.value = OnlineParameters.OFFLINE
        self.mock_request.GET.get = MagicMock(return_value='off')

        self.online_filter.apply_filter(self.mock_request)

        self.assertFalse(self.online_filter.has_changed)

    def test_online_filter_info_with_online_selected(self):

        self.online_filter.value = OnlineParameters.ONLINE

        expected_where_query = """AND dw_event.online_flag='Y' AND dw_event.country_desc IS  NULL"""
        self.assertEqual(self.online_filter.get_key(), 'online')
        self.assertEqual(self.online_filter.get_value(), OnlineParameters.ONLINE)
        self.assertEqual(self.online_filter.get_type(), 'search')
        self.assertEqual(self.online_filter.get_request_value(), {
            OnlineParameters.ONLINE.get('key'): True
        })
        self.assertEqual(self.online_filter.get_join_query(), [''])
        self.assertEqual(self.online_filter.get_where_query(), expected_where_query)

    def test_online_filter_info_without_option_selected(self):

        self.online_filter.value = None

        self.assertEqual(self.online_filter.get_key(), 'online')
        self.assertIsNone(self.online_filter.get_value())
        self.assertEqual(self.online_filter.get_type(), 'search')
        self.assertIsNone(self.online_filter.get_request_value())
        self.assertEqual(self.online_filter.get_join_query(), [''])
        self.assertEqual(self.online_filter.get_where_query(), '')

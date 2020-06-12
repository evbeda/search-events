from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.filters import EventNameFilter


class TestEventNameFilter(TestCase):

    def setUp(self):
        self.event_name_filter = EventNameFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_event_name_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='music')

        self.event_name_filter.apply_filter(self.mock_request)

        self.assertEqual(self.event_name_filter.value, 'music')
        self.assertTrue(self.event_name_filter.has_changed)

    def test_not_apply_event_name_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='')

        self.event_name_filter.apply_filter(self.mock_request)

        self.assertFalse(self.event_name_filter.has_changed)
        self.assertIsNone(self.event_name_filter.value)

    def test_apply_event_name_filter_same_value(self):
        event_name = "music"
        self.event_name_filter.value = event_name
        self.mock_request.GET.get = MagicMock(return_value='music')

        self.event_name_filter.apply_filter(self.mock_request)

        self.assertFalse(self.event_name_filter.has_changed)

    def test_event_name_filter_info_with_value(self):

        self.event_name_filter.value = "music"

        self.assertEqual(self.event_name_filter.get_join_query(), [''])
        self.assertEqual(self.event_name_filter.get_where_query(), "AND LOWER(dw_event.event_title) LIKE '%music%'")

    def test_event_name_filter_info_without_event_searched(self):

        self.event_name_filter.value = None

        self.assertEqual(self.event_name_filter.get_join_query(), [''])
        self.assertEqual(self.event_name_filter.get_where_query(), '')

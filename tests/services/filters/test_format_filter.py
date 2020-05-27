from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.models import Format
from search_events_app.filters import FormatFilter


class TestFormatFilter(TestCase):

    def setUp(self):
        self.format_filter = FormatFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_format_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='GC')

        self.format_filter.apply_filter(self.mock_request)

        self.assertEqual(self.format_filter.value.name, 'Game or Competition')
        self.assertTrue(self.format_filter.has_changed)

    def test_not_apply_format_filter(self):
        self.format_filter.apply_filter(self.mock_request)

        self.assertFalse(self.format_filter.has_changed)
        self.assertIsNone(self.format_filter.value)

    def test_apply_format_filter_with_wrong_data(self):
        self.mock_request.GET.get = MagicMock(return_value='KK')

        self.format_filter.apply_filter(self.mock_request)

        self.assertFalse(self.format_filter.has_changed)
        self.assertIsNone(self.format_filter.value)

    def test_apply_format_filter_same_value(self):
        format_ = Format.objects.get(code='GC')
        self.format_filter.value = format_
        self.mock_request.GET.get = MagicMock(return_value='GC')

        self.format_filter.apply_filter(self.mock_request)

        self.assertFalse(self.format_filter.has_changed)

    def test_format_filter_info_with_format_selected(self):

        self.format_filter.value = Format(code='GC', name='Game or Competition')

        self.assertEqual(self.format_filter.get_value(), 'Game or Competition')
        self.assertEqual(self.format_filter.get_join_query(), [''])
        self.assertEqual(self.format_filter.get_where_query(), " AND dw_cat.event_format_desc='Game or Competition' ")

    def test_format_filter_info_without_format_selected(self):

        self.format_filter.value = None

        self.assertIsNone(self.format_filter.get_value())
        self.assertEqual(self.format_filter.get_join_query(), [''])
        self.assertEqual(self.format_filter.get_where_query(), '')

from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.services.filters.features.reserved_seating_filter import ReservedSeatingFilter


class TestReserveadSeatingFilter(TestCase):

    def setUp(self):
        self.reserved_filter = ReservedSeatingFilter()

    def test_apply_reserved_seating_filter(self):
        features_codes = ['RS', 'EB']

        self.reserved_filter.apply_filter(features_codes)
        self.assertTrue(self.reserved_filter.value)
        self.assertTrue(self.reserved_filter.has_changed)

    def test_not_apply_reserved_seating_filter(self):
        features_codes = ['']

        self.reserved_filter.apply_filter(features_codes)
        self.assertFalse(self.reserved_filter.value)
        self.assertTrue(self.reserved_filter.has_changed)

    def test_apply_reserved_seating_filter_with_wrong_url_parameter(self):
        features_codes = ['text']

        result = self.reserved_filter.apply_filter(features_codes)

        self.assertIsNone(result)
        self.assertFalse(self.reserved_filter.value)
        self.assertTrue(self.reserved_filter.has_changed)

    def test_apply_reserved_seating_filter_same_value(self):
        self.reserved_filter.value = True
        features_codes = ['RS']

        self.reserved_filter.apply_filter(features_codes)

        self.assertFalse(self.reserved_filter.has_changed)

    def test_reserved_seating_filter_info_with_option_selected(self):

        self.reserved_filter.value = True

        expected_where_query = " AND dw_event.is_reserved_seating = 'Y' "
        self.assertEqual(self.reserved_filter.get_join_query(), [''])
        self.assertEqual(self.reserved_filter.get_where_query(), expected_where_query)

    def test_reserved_seating_filter_info_without_option_selected(self):

        self.reserved_filter.value = False
        self.assertEqual(self.reserved_filter.get_join_query(), [''])
        self.assertEqual(self.reserved_filter.get_where_query(), '')

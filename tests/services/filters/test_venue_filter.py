from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.filters import VenueFilter


class TestVenueFilter(TestCase):

    def setUp(self):
        self.venue_filter = VenueFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_venue_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='Maipu, Mendoza    ')

        self.venue_filter.apply_filter(self.mock_request)

        self.assertEqual(self.venue_filter.value, 'Maipu, Mendoza')
        self.assertTrue(self.venue_filter.has_changed)

    def test_not_apply_venue_filter(self):
        self.mock_request.GET.get = MagicMock(return_value=' ')

        self.venue_filter.apply_filter(self.mock_request)

        self.assertFalse(self.venue_filter.has_changed)
        self.assertIsNone(self.venue_filter.value)

    def test_apply_venue_filter_same_value(self):
        self.venue_filter.value = 'Maipu, Mendoza'
        self.mock_request.GET.get = MagicMock(return_value='Maipu, Mendoza    ')

        self.venue_filter.apply_filter(self.mock_request)

        self.assertFalse(self.venue_filter.has_changed)

    def test_venue_filter_info_with_venue_selected(self):
        expected_result = 'AND (' \
                    "LOWER(CONCAT(venue_desc, ', ', event_venue_city, ', ', " \
                    "event_venue_state, ' ', event_venue_postal_code)) " \
                    f"LIKE '%maipu, mendoza%'" \
                ')'
        self.venue_filter.value = 'Maipu, Mendoza'

        self.assertEqual(self.venue_filter.get_join_query(), [''])
        self.assertEqual(self.venue_filter.get_where_query(), expected_result)

    def test_venue_filter_info_without_venue_selected(self):

        self.venue_filter.value = None

        self.assertEqual(self.venue_filter.get_join_query(), [''])
        self.assertEqual(self.venue_filter.get_where_query(), '')

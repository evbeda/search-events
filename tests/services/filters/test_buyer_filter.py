from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.filters import BuyerFilter


class TestBuyerFilter(TestCase):

    def setUp(self):
        self.buyer_filter = BuyerFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_buyer_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='Blaine Jones')

        self.buyer_filter.apply_filter(self.mock_request)

        self.assertEqual(self.buyer_filter.value, 'Blaine Jones')
        self.assertTrue(self.buyer_filter.has_changed)

    def test_not_apply_buyer_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='')

        self.buyer_filter.apply_filter(self.mock_request)

        self.assertFalse(self.buyer_filter.has_changed)
        self.assertIsNone(self.buyer_filter.value)

    def test_apply_buyer_filter_with_blank_spaces(self):
        self.mock_request.GET.get = MagicMock(return_value='   Blaine Jones    ')

        self.buyer_filter.apply_filter(self.mock_request)

        self.assertEqual(self.buyer_filter.value, 'Blaine Jones')
        self.assertTrue(self.buyer_filter.has_changed)

    def test_apply_buyer_filter_same_value(self):
        self.buyer_filter.value = 'John Adams'
        self.mock_request.GET.get = MagicMock(return_value='John Adams')

        self.buyer_filter.apply_filter(self.mock_request)

        self.assertFalse(self.buyer_filter.has_changed)

    def test_buyer_filter_info_with_buyer_name_selected(self):

        self.buyer_filter.value = 'John Adams'
        expected_result = [
            "INNER JOIN ("\
                "SELECT event, CONCAT(first_name, ' ', last_name) AS attendee_name "\
                "FROM hive.eb.attendees "\
                "WHERE LOWER(CONCAT(first_name, ' ', last_name)) LIKE '%john adams%'"\
            ") AS at ON at.event = dw_event.event_id"
        ]

        self.assertEqual(self.buyer_filter.get_join_query(), expected_result)
        self.assertEqual(self.buyer_filter.get_where_query(), '')

    def test_buyer_filter_info_without_buyer_name_selected(self):

        self.buyer_filter.value = ''

        self.assertEqual(self.buyer_filter.get_join_query(), [''])

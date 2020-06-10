from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.filters import StartDateFilter


class TestStartDateFilter(TestCase):

    def setUp(self):
        self.start_date_filter = StartDateFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_start_date_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='2020-06-24 to 2020-06-25')

        self.start_date_filter.apply_filter(self.mock_request)
        expected_result = {
            'start': '2020-06-24',
            'end': '2020-06-25'
        }

        self.assertEqual(self.start_date_filter.value, expected_result)
        self.assertTrue(self.start_date_filter.has_changed)

    def test_not_apply_start_date_filter(self):
        self.mock_request.GET.get = MagicMock(return_value=None)

        self.start_date_filter.apply_filter(self.mock_request)

        self.assertFalse(self.start_date_filter.has_changed)
        self.assertIsNone(self.start_date_filter.value)

    def test_apply_start_date_filter_same_value(self):
        date = {
            'start': '2020-06-24',
            'end': '2020-06-25'
        }
        self.start_date_filter.value = date
        self.mock_request.GET.get = MagicMock(return_value='2020-06-24 to 2020-06-25')

        self.start_date_filter.apply_filter(self.mock_request)

        self.assertFalse(self.start_date_filter.has_changed)

    def test_start_date_filter_info_with_date_selected(self):

        self.start_date_filter.value = {
            'start': '2020-06-24',
            'end': '2020-06-25'
        }
        expected_result = "AND CAST(CAST(event_start_date AS TIMESTAMP) AS DATE)" \
                        " BETWEEN CAST('2020-06-24' AS DATE) " \
                        "AND CAST('2020-06-25' AS DATE) "

        self.assertEqual(self.start_date_filter.get_join_query(), [''])
        self.assertEqual(self.start_date_filter.get_where_query(), expected_result)

    def test_start_date_filter_info_without_date_selected(self):

        self.start_date_filter.value = None

        self.assertEqual(self.start_date_filter.get_join_query(), [''])
        self.assertEqual(self.start_date_filter.get_where_query(), '')

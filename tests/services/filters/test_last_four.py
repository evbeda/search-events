from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.filters import LastFourFilter


class TestLastFourFilter(TestCase):

    def setUp(self):
        self.last_four = LastFourFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_last_four(self):
        self.mock_request.GET.get = MagicMock(return_value='4356')

        self.last_four.apply_filter(self.mock_request)

        self.assertEqual(self.last_four.value, '4356')
        self.assertTrue(self.last_four.has_changed)

    def test_not_apply_last_four(self):
        self.mock_request.GET.get = MagicMock(return_value='')

        self.last_four.apply_filter(self.mock_request)

        self.assertFalse(self.last_four.has_changed)
        self.assertIsNone(self.last_four.value)

    def test_apply_last_four_same_value(self):
        self.last_four.value = '4356'
        self.mock_request.GET.get = MagicMock(return_value='4356')

        self.last_four.apply_filter(self.mock_request)

        self.assertFalse(self.last_four.has_changed)

    def test_last_four_info_with_last_four_selected(self):

        self.last_four.value = '4356'
        expected_result = [
                'INNER JOIN ('
                    'SELECT o.event, o.id '
                    'FROM hive.eb.orders o '
                    'INNER JOIN ('
                        'SELECT order_id '
                        'FROM hive.eb.orders_payment '
                        "WHERE last_four = '4356'"
                        ') AS op ON op.order_id = o.id'
                ') AS o on o.event = dw_event.event_id'
            ]

        self.assertEqual(self.last_four.get_join_query(), expected_result)
        self.assertEqual(self.last_four.get_where_query(), '')

    def test_last_four_info_without_last_four_selected(self):

        self.last_four.value = ''

        self.assertEqual(self.last_four.get_join_query(), [''])

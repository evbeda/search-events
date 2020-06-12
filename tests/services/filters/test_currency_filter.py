from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.models import Currency
from search_events_app.filters import CurrencyFilter


class TestCurrencyFilter(TestCase):

    def setUp(self):
        self.currency_filter = CurrencyFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_currency_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='USD')

        self.currency_filter.apply_filter(self.mock_request)

        self.assertEqual(self.currency_filter.value.code, 'USD')
        self.assertEqual(self.currency_filter.value.name, 'United States Dollar')
        self.assertTrue(self.currency_filter.has_changed)

    def test_not_apply_currency_filter(self):
        self.currency_filter.apply_filter(self.mock_request)

        self.assertFalse(self.currency_filter.has_changed)
        self.assertIsNone(self.currency_filter.value)

    def test_apply_currency_filter_with_wrong_data(self):
        self.mock_request.GET.get = MagicMock(return_value='Incorrect Currency')

        self.currency_filter.apply_filter(self.mock_request)

        self.assertFalse(self.currency_filter.has_changed)
        self.assertIsNone(self.currency_filter.value)

    def test_apply_currency_filter_same_value(self):
        currency = Currency.objects.get(code='USD')
        self.currency_filter.value = currency
        self.mock_request.GET.get = MagicMock(return_value='USD')

        self.currency_filter.apply_filter(self.mock_request)

        self.assertFalse(self.currency_filter.has_changed)

    def test_currency_filter_info_with_currency_selected(self):

        self.currency_filter.value = Currency(name='United States Dollar', code='USD')

        self.assertEqual(self.currency_filter.get_join_query(), [''])
        self.assertEqual(self.currency_filter.get_where_query(), "AND dw_event.event_currency = 'USD'")

    def test_currency_filter_info_without_currency_selected(self):

        self.currency_filter.value = None

        self.assertEqual(self.currency_filter.get_join_query(), [''])
        self.assertEqual(self.currency_filter.get_where_query(), '')

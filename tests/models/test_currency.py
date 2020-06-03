from unittest.mock import patch

from django.test import TestCase
from django.db.models import Q

from search_events_app.models import Currency


class TestCurrency(TestCase):

    def setUp(self):
        self.currency = Currency.objects.get(code='USD')

    def test_currency_basic_info(self):
        self.assertEqual(self.currency.name, 'United States Dollar')
        self.assertEqual(self.currency.code, 'USD')

    def test_currency_str(self):
        self.assertEqual(self.currency.__str__(), 'United States Dollar')

    def test_verbose_name_plural(self):
        verbose_name_plural = self.currency._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Currencies')

    @patch.object(Currency.objects, 'all')
    def test_get_context(self, mock_objects):
        categories = Currency.objects.filter(Q(code='ARS') | Q(code='USD'))
        mock_objects.return_value = categories

        expected_result = {
            'currencies': [
                {
                    'code': 'USD',
                    'name': 'United States Dollar',
                },
                {
                    'code': 'ARS',
                    'name': 'Argentine Peso',
                },
            ]
        }

        result = Currency.get_context()

        self.assertEqual(result, expected_result)

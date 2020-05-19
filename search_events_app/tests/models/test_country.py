from unittest.mock import (
	MagicMock,
	patch,
)

from django.test import TestCase
from django.db.models import Q

from search_events_app.models.country import Country


class TestCountry(TestCase):

    def setUp(self):
        self.country = Country.objects.get(name='Argentina')

    def test_country_basic_info(self):
        self.assertEqual(self.country.name, 'Argentina')
        self.assertEqual(self.country.alpha_2_code, 'AR')

    def test_country_str(self):
        self.assertEqual(self.country.__str__(), 'Argentina')

    @patch.object(Country.objects, 'all')
    def test_get_context(self, mock_objects):
        countries = Country.objects.filter(Q(name='Peru') | Q(name='Spain'))

        mock_objects.return_value = countries
        expected_result = {
            'countries': [
                {
                    'alpha2Code': 'PE',
                    'name': 'Peru',
                },
                {
                    'alpha2Code': 'ES',
                    'name': 'Spain',
                }
            ]
        }

        result = Country.get_context()

        self.assertEqual(result, expected_result)

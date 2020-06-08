from unittest.mock import patch

from django.test import TestCase

from search_events_app.models import Country


class TestCountry(TestCase):

    def setUp(self):
        self.country = Country.objects.get(name='Argentina')

    def test_country_basic_info(self):
        self.assertEqual(self.country.name, 'Argentina')
        self.assertEqual(self.country.alpha_2_code, 'AR')

    def test_country_str(self):
        self.assertEqual(self.country.__str__(), 'Argentina')

    def test_verbose_name_plural(self):
        verbose_name_plural = self.country._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Countries')

    @patch.object(Country.objects, 'all')
    @patch.object(Country, 'get_cities')
    def test_get_context(self, mock_cities, mock_all):
        countries = Country.objects.filter(name='Argentina')
        cities = [
            {
                'code': '',
                'name': 'Mendoza',
            }
        ]
        mock_cities.return_value = cities
        mock_all.return_value = countries

        expected_result = {
            'countries': [
                {
                    'code': 'AR',
                    'name': 'Argentina',
                    'cities': cities,
                },
            ]
        }

        result = Country.get_context()

        self.assertEqual(result, expected_result)

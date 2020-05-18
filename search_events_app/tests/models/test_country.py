from unittest.mock import (
	MagicMock,
	patch,
)

from django.test import TestCase

from search_events_app.models.country import Country


class TestCountry(TestCase):

    def setUp(self):
        self.country = Country.objects.create(label='Argentina', code='AR',
        eventbrite_id='1234')

    def test_country_basic_info(self):
        self.assertEqual(self.country.name, 'Argentina')
        self.assertEqual(self.country.alpha_2_code, 'AR')
        self.assertEqual(self.country.eventbrite_id, '1234')

    def test_country_str(self):
        self.assertEqual(self.country.__str__(), 'Argentina')

    @patch.object(
		Country,
		'objects'
	)
    def test_get_context(self, mock_objects):
        countries = [
			Country(label='Argentina', code='AR', eventbrite_id='1234'),
			Country(label='Spain', code='ES', eventbrite_id='4567')
		]
        
        mock_objects.all = MagicMock(return_value=countries)

        expected_result = {
            'countries': [
                {
                    'alpha2Code': 'AR',
                    'name': 'Argentina'
                },
                {
                    'alpha2Code': 'ES',
                    'name': 'Spain'
                }
            ]
        }

        result = Country.get_context()

        self.assertEqual(result, expected_result)
    
from unittest.mock import patch

from django.test import TestCase

from search_events_app.models.event import Event
from search_events_app.services import api_service
from search_events_app.services.dummy_api import DummyApi


class TestApiService(TestCase):

    def setUp(self):
        self.mock_api_response = [
            {
                'name': 'Carats world tour',
                'organizer_name': 'Seung',
                'country': 'Italy',
                'url': 'https://www.eventbrite.com/e/carats-world-tour-tickets-102537931714?aff=ebdssbonlinesearch',
                'start_date': '2020-07-20',
                'features': ['EB Studio'],
                'language': 'English',
                'category': 'Music',
                'format': 'Festival'
            },
            {
                'name': 'Virtual stitch & bitch',
                'organizer_name': 'Fashion Revolution',
                'country': '',
                'url': 'https://www.eventbrite.co.uk/e/fashion-question-time-tickets-90925824589?aff=ebdssbonlinesearch',
                'start_date': '2021-01-30',
                'features': ['Repeating event'],
                'language': 'English',
                'category': 'Fashion',
                'format': 'Expo',
            },
        ]

    def test_get_events(self):
        with patch.object(
            DummyApi,
            'get',
            return_value=self.mock_api_response
        ):
            result = api_service.get_events()
            self.assertIsInstance(result[0], Event)
            self.assertEqual(len(result), 2)

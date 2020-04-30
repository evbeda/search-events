from unittest.mock import (
    patch,
    MagicMock,
)

from django.test import TestCase

from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.services.api_service import ApiService
from search_events_app.services.dummy_api import DummyApi


class TestApiService(TestCase):

    def setUp(self):
        self.mock_api_response = {
            'events': {
                'results': [
                    {
                        'name': 'Carats world tour',
                        'primary_organizer': {
                            "name": "MusicABC_2"
                        },
                        'primary_venue': {
                            'address': {
                                'country': 'US',
                            }
                        },
                        'url': 'https://www.eventbrite.com/e/carats-world-tour-tickets-102537931714?aff=ebdssbonlinesearch',
                        'start_date': '2020-07-20',
                        'language': 'en-us',
                        'tags': [
                            {
                                "prefix": "EventbriteCategory",
                                "display_name": "Music"
                            },
                            {
                                "prefix": "EventbriteFormat",
                                "display_name": "Festival"
                            },
                        ]
                    },
                    {
                        'name': 'Virtual stitch & bitch',
                        'primary_organizer': {
                            "name": "MusicABC"
                        },
                        'primary_venue': {
                            'address': {
                                'country': 'GB',
                            }
                        },
                        'url': 'https://www.eventbrite.co.uk/e/fashion-question-time-tickets-90925824589?aff=ebdssbonlinesearch',
                        'start_date': '2021-01-30',
                        'language': 'en-gb',
                        'tags': [
                            {
                                "prefix": "EventbriteCategory",
                                "display_name": "Fashion"
                            },
                            {
                                "prefix": "EventbriteFormat",
                                "display_name": "Expo"
                            },
                        ]
                    },
                ]
            }
        }

    @patch(
        'search_events_app.services.api_service.requests.post'
    )
    def test_get_events(self, mock_post):
        country1 = Country.objects.create(
            name='England',
            alpha2Code='GB',
            alpha3Code='GBT',
            flag='https://www.google.com.ar'
        )
        country2 = Country.objects.create(
            name='United States',
            alpha2Code='US',
            alpha3Code='USA',
            flag='https://www.google.com.ar'
        )
        response = MagicMock()
        response.json = MagicMock(return_value=self.mock_api_response)
        mock_post.return_value = response
        result = ApiService().get_events()
        self.assertIsInstance(result[0], Event)
        self.assertEqual(len(result), 2)

from unittest.mock import (
    MagicMock,
    patch,
)

from django.test import TestCase

from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.services.api.api_service import ApiService
from search_events_app.dto.dto_api_service_filter import DTOApiServiceFilter


class TestApiService(TestCase):

    def setUp(self):
        self.mock_dto_filter = [DTOApiServiceFilter(type='search', value={'places_within': '1234'})]
        self.mock_api_response = {
            'events': {
                'results': [
                    {
                        'name': 'Carats world tour',
                        'primary_organizer': {
                            'name': 'MusicABC_2'
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
                                'prefix': 'EventbriteCategory',
                                'display_name': 'Music'
                            },
                            {
                                'prefix': 'EventbriteFormat',
                                'display_name': 'Festival'
                            },
                        ]
                    },
                    {
                        'name': 'Virtual stitch & bitch',
                        'primary_organizer': {
                            'name': 'MusicABC'
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
                                'prefix': 'EventbriteCategory',
                                'display_name': 'Fashion'
                            },
                            {
                                'prefix': 'EventbriteFormat',
                                'display_name': 'Expo'
                            },
                        ]
                    },
                ]
            }
        }
        self.mock_response_processed = [
            {
                'name': 'Event1',
                'url': 'www.google',
                'language': 'Spanish',
                'start_date': '2020-05-12',
                'category': 'category A',
                'format_': 'format A',
                'organizer': 'Organizer 1',
                'country': 'Argentina'
            },
            {
                'name': 'Event2',
                'url': 'www.google',
                'language': 'Spanish',
                'start_date': '2020-05-12',
                'category': 'category A',
                'format_': 'format A',
                'organizer': 'Organizer 1',
                'country': 'Argentina',
            }
        ]

    @patch.object(
        ApiService,
        'format_body'
    )
    @patch(
        'search_events_app.services.api.api_service.requests.post'
    )
    @patch(
        'search_events_app.services.api.api_service.process_events'
    )
    def test_get_events(self, mock_process_events, mock_post, mock_format_body):
        post_response = MagicMock()
        post_response.json = MagicMock(return_value=self.mock_api_response)
        mock_post.return_value = post_response
        mock_process_events.return_value = self.mock_response_processed

        result = ApiService.get_events(dto_filters_array=self.mock_dto_filter)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Event)
        self.assertIsInstance(result[1], Event)

    def test_format_body(self):
        expected = {
            'event_search': {
                'sort': 'default',
                'dates': 'current_future',
                'page_size': 40,
                'places_within': '1234'
            }
        }

        result = ApiService.format_body(self.mock_dto_filter)

        self.assertEqual(result, expected)

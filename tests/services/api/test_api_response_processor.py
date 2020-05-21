from django.test import TestCase

from search_events_app.services.api.api_response_processor import (
    get_country,
    get_language,
    get_tag,
    get_url,
    process_events,
)


class TestApiResponseProcessor(TestCase):
    def test_process_events(self):
        mock_api_response = {
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

        result = process_events(mock_api_response)
        expected_result = {
            'name': 'Carats world tour',
            'url': 'https://www.eventbrite.com/e/carats-world-tour-tickets-102537931714?aff=ebdssbonlinesearch',
            'language': 'en',
            'start_date': '2020-07-20',
            'category': 'Music',
            'format_': 'Festival',
            'organizer': 'MusicABC_2',
            'country': 'United States',
        }

        self.assertIsInstance(result[0], dict)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], expected_result)

    def test_get_tag(self):
        item = {
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
        }

        category = get_tag(item, 'EventbriteCategory')
        format_ = get_tag(item, 'EventbriteFormat')

        self.assertEqual(category, 'Music')
        self.assertEqual(format_, 'Festival')

    def test_get_tag_without_category(self):
        item = {
            'tags': [
                {
                    'prefix': 'EventbriteFormat',
                    'display_name': 'Festival'
                },
            ]
        }

        category = get_tag(item, 'EventbriteCategory')

        self.assertIsNone(category)

    def test_get_country(self):
        item = {
            'primary_venue': {
                'address': {
                    'country': 'GB'
                },
            }
        }

        country = get_country(item)

        self.assertEqual(country, 'United Kingdom')

    def test_get_none_country(self):
        item = {
            'primary_venue': {
                'address': {
                    'city': 'Amsterdam'
                },
            }
        }

        country = get_country(item)

        self.assertIsNone(country)
     
    def test_language(self):
        item = {
            'language': 'en-gb'
        }

        result = get_language(item)

        self.assertEqual(result, "en")

    def test_url(self):
        item = {
            'url': 'https://www.evbqa.com/evento-de-prueba'
        }

        result = get_url(item)

        self.assertEqual(result, 'https://www.eventbrite.com/evento-de-prueba')

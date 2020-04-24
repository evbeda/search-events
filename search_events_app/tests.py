from unittest.mock import patch

from django.test import TestCase

from search_events_app.services import api_service
from search_events_app.services.dummy_api import DummyApi
from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.models.feature import Feature


class TestModels(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Argentina", alpha_2_code="AR",
        alpha_3_code="ARG", flag="https://restcountries.eu/data/arg.svg")
        self.feature = Feature("Embedded Checkout")
        self.feature2 = Feature("Reserved Seating")
        self.event = Event(
            "Evento1", "www.google" +
            ".com", self.country, self.feature
            )
        self.event2 = Event("Name", "www.google.com")
        self.new_event = Event(
            "Futbol",
            "www.google.com",
            feature=[self.feature, self.feature2]
            )
        self.dict_event = {
                'name': 'Carats world tour',
                'organizer_name': 'Seung',
                'country': 'Italy',
                'url': (
                    'https://www.eventbrite.com/e/carats-world-tour-tickets'
                    '-102537931714?aff=ebdssbonlinesearch'
                    ),
                'start_date': '2020-07-20',
                'features': ['EB Studio', 'Facebook'],
                'language': 'English',
                'category': 'Music',
                'format': 'Festival'
            }

    def test_feature_model(self):
        self.assertEqual(self.feature.name, "Embedded Checkout")

    def test_country_model(self):
        self.assertEqual(self.country.name, "Argentina")
        self.assertEqual(self.country.alpha_2_code, "AR")
        self.assertEqual(self.country.alpha_3_code, "ARG")
        self.assertEqual(self.country.flag, "https://restcountries.eu/data/arg.svg")

    def test_event_model(self):
        self.assertEqual(self.event2.country, None)
        self.assertEqual(self.event.name, "Evento1")
        self.assertEqual(self.event.country, self.country)
        self.assertEqual(self.event.feature, self.feature)
        self.assertEqual(self.event2.url, "www.google.com")

    def test_event_with_two_features(self):
        self.assertEqual(len(self.new_event.feature), 2)

    def test_events_more_items(self):
        event_more_items = Event(**self.dict_event)
        self.assertEqual(event_more_items.language, 'English')
        self.assertEqual(event_more_items.category, 'Music')
        self.assertEqual(event_more_items.format, 'Festival')


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

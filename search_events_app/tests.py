from unittest.mock import patch

from django.test import TestCase

from search_events_app.services import api_service
from search_events_app.services.dummy_api import DummyApi
from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.models.feature import Feature


class TestCountry(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name="Argentina", alpha2Code="AR",
        alpha3Code="ARG", flag="https://restcountries.eu/data/arg.svg")

    def test_country_basic_info(self):
        self.assertEqual(self.country.name, "Argentina")
        self.assertEqual(self.country.alpha_2_code, "AR")
        self.assertEqual(self.country.alpha_3_code, "ARG")
        self.assertEqual(self.country.flag, "https://restcountries.eu/data/arg.svg")

    def test_country_str(self):
        self.assertEqual(self.country.__str__(), "Argentina")

    
class TestEvent(TestCase):

    def setUp(self):
        self.feature = Feature("Embedded Checkout")

    def test_event_without_country(self):
        event = Event("Name", "www.google.com")
        self.assertEqual(event.country, None)

    
    def test_event_basic_info(self):
        country = Country.objects.create(name="Argentina", alpha2Code="AR",
        alpha3Code="ARG", flag="https://restcountries.eu/data/arg.svg")
        event = Event(
            "Evento1", "www.google" +
            ".com", country, self.feature
        )
        self.assertEqual(event.name, "Evento1")
        self.assertEqual(event.country, country)
        self.assertEqual(event.feature, self.feature)
        self.assertEqual(event.url, "www.google.com")

    def test_event_with_two_features(self):
        feature = Feature("Reserved Seating")        
        event = Event(
            "Futbol",
            "www.google.com",
            feature=[self.feature, feature]
        )
        self.assertEqual(len(event.feature), 2)

    def test_events_more_items(self):
        dict_event = {
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
        event = Event(**dict_event)
        self.assertEqual(event.language, 'English')
        self.assertEqual(event.category, 'Music')
        self.assertEqual(event.format, 'Festival')    


class TestFeature(TestCase):

    def test_feature_model(self):
        feature = Feature("Embedded Checkout")
        self.assertEqual(feature.name, "Embedded Checkout")


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

from django.test import TestCase

from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.models.feature import Feature


class TestModels(TestCase):
    def setUp(self):
        self.country = Country("Argentina")
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

    def test_feature_model(self):
        self.assertEqual(self.feature.name, "Embedded Checkout")

    def test_country_model(self):
        self.assertEqual(self.country.name, "Argentina")

    def test_event_model(self):
        self.assertEqual(self.event2.country, None)
        self.assertEqual(self.event.name, "Evento1")
        self.assertEqual(self.event.country, self.country)
        self.assertEqual(self.event.feature, self.feature)
        self.assertEqual(self.event2.url, "www.google.com")

    def test_event_with_two_features(self):
        self.assertEqual(len(self.new_event.feature), 2)

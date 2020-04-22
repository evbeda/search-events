from django.test import TestCase
from .models.country import Country
from .models.event import Event
from .models.feature import Feature


class TestModels(TestCase):
    def setUp(self):
        self.country = Country("Argentina")
        self.feature = Feature("Embedded Checkout")
        self.event = Event("Evento1", self.country, self.feature)

    def test_feature_model(self):
        self.assertEqual(self.feature.name, "Embedded Checkout")

    def test_country_model(self):
        self.assertEqual(self.country.name, "Argentina")

    def test_event_model(self):
        self.event2 = Event("Name")
        self.assertEqual(self.event2.country, None)
        self.assertEqual(self.event.name, "Evento1")
        self.assertEqual(self.event.country, self.country)
        self.assertEqual(self.event.feature, self.feature)

    def test_event_with_two_features(self):
        self.feature2 = Feature("Reserved Seating")
        self.new_event = Event("Futbol", feature=[self.feature, self.feature2])
        self.assertEqual(len(self.new_event.feature), 2)

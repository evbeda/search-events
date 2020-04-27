from django.test import TestCase

from search_events_app.models.feature import Feature

    
class TestFeature(TestCase):

    def test_feature_model(self):
        feature = Feature("Embedded Checkout")
        self.assertEqual(feature.name, "Embedded Checkout")

from django.test import TestCase

from search_events_app.models.feature import Feature

    
class TestFeature(TestCase):

    def setUp(self):
        self.feature = Feature.objects.create(name='Embedded Checkout', code='EC')

    def test_feature_model(self):
        self.assertEqual(self.feature.name, 'Embedded Checkout')

    def test_feature_str(self):
        self.assertEqual(self.feature.__str__(), 'Embedded Checkout')

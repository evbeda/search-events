from django.test import TestCase

from search_events_app.models.feature import Feature

    
class TestFeature(TestCase):

    def setUp(self):
        self.feature = Feature.objects.create(name='Embedded Checkout', code='EC')

    def test_feature_model(self):
        feature = Feature('Website Widgets')
        self.assertEqual(feature.name, 'Website Widgets')

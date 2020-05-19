from django.test import TestCase

from search_events_app.models.feature import Feature

    
class TestFeature(TestCase):

    def setUp(self):
        self.feature = Feature.objects.create(name='Website Widgets', code='WW')

    def test_feature_model(self):
        self.assertEqual(self.feature.name, 'Website Widgets')

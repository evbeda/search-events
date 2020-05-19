from unittest.mock import patch

from django.db.models import Q
from django.test import TestCase

from search_events_app.models.feature import Feature

    
class TestFeature(TestCase):

    def setUp(self):
        self.feature = Feature.objects.create(name='Website Widgets', code='WW')

    def test_feature_model(self):
        self.assertEqual(self.feature.name, 'Website Widgets')

    @patch.object(Feature.objects, 'all')
    def test_get_context(self, mock_objects):
        features = Feature.objects.filter(Q(code='AO') | Q(code='RS'))
        mock_objects.return_value = features

        expected_result = {
            'features': [
                {
                    'code': 'RS',
                    'name': 'Reserved Seating',
                },
                {
                    'code': 'AO',
                    'name': 'Add Ons',
                },
            ]
        }

        result = Feature.get_context()

        self.assertEqual(result, expected_result)


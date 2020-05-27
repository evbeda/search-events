from unittest.mock import patch

from django.db.models import Q
from django.test import TestCase

from search_events_app.models import Feature
from search_events_app.utils import FeatureCodes


class TestFeature(TestCase):

    def setUp(self):
        self.feature = Feature.objects.create(name='Website Widgets', code='WW')

    def test_feature_model(self):
        self.assertEqual(self.feature.name, 'Website Widgets')

    def test_feature_str(self):
        self.assertEqual(self.feature.__str__(), 'Website Widgets')

    def test_verbose_name_plural(self):
        verbose_name_plural = self.feature._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Features')

    @patch.object(Feature.objects, 'all')
    def test_get_context(self, mock_objects):
        features = Feature.objects.filter(Q(code=FeatureCodes.add_ons) | Q(code=FeatureCodes.reserved_seating))
        mock_objects.return_value = features

        expected_result = {
            'features': [
                {
                    'code': 'AO',
                    'name': 'Add Ons',
                },
                {
                    'code': 'RS',
                    'name': 'Reserved Seating',
                },
            ]
        }

        result = Feature.get_context()

        self.assertEqual(result, expected_result)


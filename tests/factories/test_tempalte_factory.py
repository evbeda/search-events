from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.factories import TemplateFactory


class TestTemplateFactory(TestCase):

    def test_get_template_factory_for_specific_events(self):
        mock_request = MagicMock()
        mock_request.path = 'SpecificEvent'

        result = TemplateFactory.get_template(mock_request)

        self.assertEqual(result, 'specific_event.html')

    def test_get_template_factory_for_find_feature(self):
        mock_request = MagicMock()
        mock_request.path = 'FindFeature'

        result = TemplateFactory.get_template(mock_request)

        self.assertEqual(result, 'find_feature.html')

    def test_get_template_factory_with_wrong_url(self):
        mock_request = MagicMock()
        mock_request.path = 'test'

        result = TemplateFactory.get_template(mock_request)

        self.assertIsNone(result)

from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.factories.query_parameter_factory import QueryParameterFactory
from search_events_app.utils import SpecificEventsQueryParameters, FindFeatureQueryParameters


class TestQueryParameterFactory(TestCase):

    def test_get_query_parameters_for_specific_events(self):
        mock_request = MagicMock()
        mock_request.path = 'SpecificEvent'

        result = QueryParameterFactory.get_query_parameters(mock_request)

        self.assertEqual(result, SpecificEventsQueryParameters)

    def test_get_query_parameters_for_find_feature(self):
        mock_request = MagicMock()
        mock_request.path = 'FindFeature'

        result = QueryParameterFactory.get_query_parameters(mock_request)

        self.assertEqual(result, FindFeatureQueryParameters)

    def test_get_query_parameters_with_wrong_url(self):
        mock_request = MagicMock()
        mock_request.path = 'test'

        result = QueryParameterFactory.get_query_parameters(mock_request)

        self.assertIsNone(result)

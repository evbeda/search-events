from unittest.mock import (
    MagicMock,
    patch,
)

from django.test import TestCase

from search_events_app.services.filters import FeatureFilterManager
from search_events_app.services.filters.features import (
    AddOnsFilter,
    RepeatingEventsFilter,
    ReservedSeatingFilter,
    WebsiteWidgetsFilter,
)
from search_events_app.utils.feature_codes import FeatureCodes


class TestFeatureFilterManager(TestCase):
    def setUp(self):
        self.feature_filter_manager = FeatureFilterManager()

    @patch.object(AddOnsFilter, 'apply_filter')
    def test_feature_filter_add_ons(self, patch_apply):
        mock_request = MagicMock()
        mock_request.GET = MagicMock()
        mock_request.GET.get = MagicMock(return_value=FeatureCodes.add_ons)
        self.feature_filter_manager.latest_filters = [AddOnsFilter(), AddOnsFilter()]
        self.feature_filter_manager.apply_filter(mock_request)
        count = patch_apply.call_count
        self.assertEqual(count, 1)

    def test_feature_filter_manager_has_changed_true(self):
        mock_request = MagicMock()
        mock_request.GET = MagicMock()
        mock_request.GET.get = MagicMock(return_value=FeatureCodes.add_ons)
        self.feature_filter_manager.latest_filters = [AddOnsFilter(), RepeatingEventsFilter(), ReservedSeatingFilter()]

        self.feature_filter_manager.apply_filter(mock_request)

        self.assertTrue(self.feature_filter_manager.has_changed)

    def test_feature_filter_manager_has_changed_false(self):
        self.feature_filter_manager.latest_filters = [AddOnsFilter(), RepeatingEventsFilter(), WebsiteWidgetsFilter()]

        self.assertFalse(self.feature_filter_manager.has_changed)

    def test_feature_filter_manager_info_with_add_on_selected(self):
        mock_request = MagicMock()
        mock_request.GET = MagicMock()
        mock_request.GET.get = MagicMock(return_value=FeatureCodes.add_ons)
        self.feature_filter_manager.latest_filters = [AddOnsFilter(), RepeatingEventsFilter(), WebsiteWidgetsFilter()]

        self.feature_filter_manager.apply_filter(mock_request)

        self.assertEqual(self.feature_filter_manager.get_key(), '')
        self.assertEqual(self.feature_filter_manager.get_value(), '')
        self.assertEqual(self.feature_filter_manager.get_type(), '')
        self.assertEqual(self.feature_filter_manager.get_request_value(), '')
        self.assertEqual(self.feature_filter_manager.get_join_query(), [''])
        self.assertEqual(self.feature_filter_manager.get_where_query(), " AND f.trx_type = 'add_on_ticket_purchase'")

    def test_feature_filter_manager_info_without_selected(self):
        mock_request = MagicMock()
        mock_request.GET = MagicMock()
        mock_request.GET.get = MagicMock(return_value='')
        self.feature_filter_manager.latest_filters = [AddOnsFilter(), RepeatingEventsFilter(), WebsiteWidgetsFilter()]

        self.feature_filter_manager.apply_filter(mock_request)

        self.assertEqual(self.feature_filter_manager.get_key(), '')
        self.assertEqual(self.feature_filter_manager.get_value(), '')
        self.assertEqual(self.feature_filter_manager.get_type(), '')
        self.assertEqual(self.feature_filter_manager.get_request_value(), '')
        self.assertEqual(self.feature_filter_manager.get_join_query(), [''])
        self.assertEqual(self.feature_filter_manager.get_where_query(), '')

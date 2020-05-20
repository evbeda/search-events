from django.test import TestCase

from search_events_app.services.filters.features.add_ons_filter import AddOnsFilter
from search_events_app.utils.feature_codes import FeatureCodes


class TestAddOnsFilter(TestCase):

    def setUp(self):
        self.add_ons_filter = AddOnsFilter()

    def test_apply_add_ons_filter(self):
        self.add_ons_filter.apply_filter([FeatureCodes.add_ons, FeatureCodes.repeating_events, FeatureCodes.reserved_seating])
        
        self.assertTrue(self.add_ons_filter.value)

    def test_apply_without_add_ons_filter(self):
        self.add_ons_filter.apply_filter([FeatureCodes.repeating_events, FeatureCodes.reserved_seating])
        
        self.assertFalse(self.add_ons_filter.value)

    def test_join_query(self):
        self.add_ons_filter.value = True
        result = self.add_ons_filter.get_join_query()

        self.assertEqual(result, ['INNER JOIN dw.f_ticket_merchandise_purchase f ON f.event_id = dw_event.event_id'])

    def test_join_query_value_false(self):
        self.add_ons_filter.value = False
        result = self.add_ons_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_where_query_value_true(self):
        self.add_ons_filter.value = True

        result = self.add_ons_filter.get_where_query()

        self.assertEqual(result, " AND f.trx_type = 'add_on_ticket_purchase'")

    def test_where_query_value_false(self):
        self.add_ons_filter.value = False

        result = self.add_ons_filter.get_where_query()

        self.assertEqual(result, '')

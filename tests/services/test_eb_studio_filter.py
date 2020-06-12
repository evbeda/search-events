from django.test import TestCase

from search_events_app.filters.features import EBStudioFilter
from search_events_app.utils import FeatureCodes


class TestEBStudioFilter(TestCase):

    def setUp(self):
        self.eb_studio_filter = EBStudioFilter()

    def test_apply_eb_studio_filter(self):
        self.eb_studio_filter.apply_filter(
            [FeatureCodes.eventbrite_studio, FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertTrue(self.eb_studio_filter .value)

    def test_apply_without_group_registration_filter(self):
        self.eb_studio_filter.apply_filter([FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertFalse(self.eb_studio_filter.value)

    def test_join_query(self):
        result = self.eb_studio_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_where_query_with_false_value(self):
        self.eb_studio_filter.value = False

        result = self.eb_studio_filter.get_where_query()

        self.assertEqual(result, '')

    def test_where_query_with_true_value(self):
        self.eb_studio_filter.value = True

        result = self.eb_studio_filter.get_where_query()

        self.assertEqual(result, 'AND es.domain IS NOT NULL')

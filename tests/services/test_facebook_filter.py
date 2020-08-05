from django.test import TestCase

from search_events_app.filters.features import FacebookFilter
from search_events_app.utils import FeatureCodes


class TestFacebookFilter(TestCase):

    def setUp(self):
        self.facebook_filter = FacebookFilter()

    def test_apply_facebook_filter(self):
        self.facebook_filter.apply_filter(
            [FeatureCodes.facebook, FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertTrue(self.facebook_filter.value)

    def test_apply_without_facebook_filter(self):
        self.facebook_filter.apply_filter([FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertFalse(self.facebook_filter.value)

    def test_join_query_value_false(self):
        result = self.facebook_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_join_query_value_true(self):
        self.facebook_filter.value = True
        result = self.facebook_filter.get_join_query()
        self.assertEqual(result, [
            'INNER JOIN ('
                'SELECT facebook_event_id, event_id '
                'FROM hive.web.facebookpublishevent_action'
            ') AS fb ON dw_event.event_id = fb.event_id'
        ])

    def test_where_query(self):
        self.facebook_filter.value = False

        result = self.facebook_filter.get_where_query()

        self.assertEqual(result, '')

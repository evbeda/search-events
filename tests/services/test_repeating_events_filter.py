from django.test import TestCase

from search_events_app.filters.features import RepeatingEventsFilter


class TestRepeatingEventsFilter(TestCase):

    def setUp(self):
        self.filter = RepeatingEventsFilter()

    def test_apply_filter_with_changes(self):
        self.filter.value = False
        feature_codes = 'HG-RE-AS'

        self.filter.apply_filter(feature_codes)

        self.assertTrue(self.filter.has_changed)
        self.assertTrue(self.filter.value)

    def test_apply_filter_without_changes(self):
        self.filter.value = True
        feature_codes = 'HG-RE-AS'

        self.filter.apply_filter(feature_codes)

        self.assertFalse(self.filter.has_changed)
        self.assertTrue(self.filter.value)

    def test_get_join_query(self):

        result = self.filter.get_join_query()
        self.assertEqual(result, [''])

    def test_get_where_query_with_filter_applied(self):
        self.filter.value = True

        result = self.filter.get_where_query()
        self.assertEqual(result, " AND dw_event.is_repeating_event = 'Y'")

    def test_get_where_query_without_filter_applied(self):
        self.filter.value = False

        result = self.filter.get_where_query()
        self.assertEqual(result, '')

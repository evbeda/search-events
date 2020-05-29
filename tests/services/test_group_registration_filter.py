from django.test import TestCase

from search_events_app.filters.features import GroupRegistrationFilter
from search_events_app.utils import FeatureCodes


class TestGroupRegistrationFilter(TestCase):

    def setUp(self):
        self.group_registration_filter = GroupRegistrationFilter()

    def test_apply_group_registration_filter(self):
        self.group_registration_filter.apply_filter([FeatureCodes.group_registration, FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertTrue(self.group_registration_filter.value)

    def test_apply_without_group_registration_filter(self):
        self.group_registration_filter.apply_filter([FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertFalse(self.group_registration_filter.value)

    def test_join_query_value_false(self):
        result = self.group_registration_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_join_query_value_true(self):
        self.group_registration_filter.value = True
        result = self.group_registration_filter.get_join_query()
        
        self.assertEqual(result, ['INNER JOIN ('\
                'SELECT event_id '\
                'FROM hive.eb.team'\
                ') AS team ON dw_event.event_id = team.event_id'
                ])

    def test_where_query_(self):
        self.group_registration_filter.value = False

        result = self.group_registration_filter.get_where_query()

        self.assertEqual(result, '')

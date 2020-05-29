from django.test import TestCase

from search_events_app.filters.features import DonationFilter
from search_events_app.utils import FeatureCodes


class TestDonationFilter(TestCase):

    def setUp(self):
        self.donation_filter = DonationFilter()

    def test_apply_donation_filter(self):
        self.donation_filter.apply_filter([FeatureCodes.donation, FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertTrue(self.donation_filter.value)

    def test_apply_without_donation_filter(self):
        self.donation_filter.apply_filter([FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertFalse(self.donation_filter.value)

    def test_join_query_value_true(self):
        self.donation_filter.value = True
        result = self.donation_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_join_query_value_false(self):
        result = self.donation_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_where_query_value_true(self):
        self.donation_filter.value = True

        result = self.donation_filter.get_where_query()

        self.assertEqual(result, ' AND ts.donation > 0 ')

    def test_where_query_value_false(self):
        self.donation_filter.value = False

        result = self.donation_filter.get_where_query()

        self.assertEqual(result, '')

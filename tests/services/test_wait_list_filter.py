from django.test import TestCase

from search_events_app.filters.features import WaitlistFilter
from search_events_app.utils import FeatureCodes


class TestWaitlistFilter(TestCase):

    def setUp(self):
        self.waitlist_filter = WaitlistFilter()

    def test_apply_waitlist_filter(self):
        self.waitlist_filter.apply_filter([FeatureCodes.wait_list, FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertTrue(self.waitlist_filter.value)

    def test_apply_without_waitlist_filter(self):
        self.waitlist_filter.apply_filter([FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertFalse(self.waitlist_filter.value)

    def test_join_query_value_true(self):
        self.waitlist_filter.value = True
        result = self.waitlist_filter.get_join_query()
        result_query = ["""
            INNER JOIN (
                SELECT hive.eb.waitlist.event, ticket
                FROM hive.eb.waitlist
                INNER JOIN (
                    SELECT id
                    FROM hive.eb.ticket_classes
                    WHERE (
                        quantity_sold >= quantity_total
                        AND is_donation = 0
                        AND quantity_total > 0
                        AND DATE(CAST(start_sales AS TIMESTAMP)) < NOW() - INTERVAL '1' DAY
                        AND DATE(CAST(end_sales AS TIMESTAMP)) > NOW() + INTERVAL '1' MONTH
                        AND delete = 'n'
                    )
                ) AS tc ON tc.id = hive.eb.waitlist.ticket
            ) AS waitlist ON waitlist.event = dw_event.event_id
            """]

        self.assertEqual(result, result_query)

    def test_join_query_value_false(self):
        result = self.waitlist_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_where_query_value_false(self):
        self.waitlist_filter.value = False

        result = self.waitlist_filter.get_where_query()

        self.assertEqual(result, '')

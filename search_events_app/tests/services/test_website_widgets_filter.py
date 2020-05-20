from django.test import TestCase

from search_events_app.services.filters.features.website_widgets_filter import WebsiteWidgetsFilter
from search_events_app.utils.feature_codes import FeatureCodes


class TestWebsiteWidgetsFilter(TestCase):

    def setUp(self):
        self.website_widgets_filter = WebsiteWidgetsFilter()

    def test_apply_website_widgets_filter(self):
        self.website_widgets_filter.apply_filter([FeatureCodes.website_widgets, FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertTrue(self.website_widgets_filter.value)

    def test_apply_without_website_widgets_filter(self):
        self.website_widgets_filter.apply_filter([FeatureCodes.repeating_events, FeatureCodes.reserved_seating])

        self.assertFalse(self.website_widgets_filter.value)

    def test_join_query_value_true(self):
        self.website_widgets_filter.value = True
        result = self.website_widgets_filter.get_join_query()

        self.assertEqual(result, ['INNER JOIN dw.f_ticket_merchandise_purchase f ON f.event_id = dw_event.event_id', 'INNER JOIN dw.dim_affiliate_code_group dacg ON dacg.affiliate_code = f.q_order_affiliate_code'])

    def test_join_query_value_false(self):
        result = self.website_widgets_filter.get_join_query()

        self.assertEqual(result, [''])

    def test_join_query_value_true(self):
        self.website_widgets_filter.value = True
        result = self.website_widgets_filter.get_join_query()
        self.assertEqual(result, ['INNER JOIN ('\
                    'SELECT affiliate_code, affiliate_group_2 '\
                    'FROM hive.dw.dim_affiliate_code_group'\
                ') AS dacg ON dacg.affiliate_code = f.q_order_affiliate_code'
                ])

    def test_where_query_value_true(self):
        self.website_widgets_filter.value = True

        result = self.website_widgets_filter.get_where_query()

        self.assertEqual(result, " AND dacg.affiliate_group_2 = 'Website Widgets'")

    def test_where_query_value_false(self):
        self.website_widgets_filter.value = False

        result = self.website_widgets_filter.get_where_query()

        self.assertEqual(result, '')

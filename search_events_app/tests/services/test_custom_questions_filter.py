from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.services.filters.features import CustomQuestionFilter


class TestCustomQuestionFilter(TestCase):

    def setUp(self):
        self.custom_question_filter = CustomQuestionFilter()

    def test_apply_custom_question_filter(self):
        features_codes = ['CQ', 'EB']

        self.custom_question_filter.apply_filter(features_codes)

        self.assertTrue(self.custom_question_filter.value)
        self.assertTrue(self.custom_question_filter.has_changed)

    def test_not_apply_custom_question_filter(self):
        features_codes = ['']

        self.custom_question_filter.apply_filter(features_codes)

        self.assertFalse(self.custom_question_filter.value)
        self.assertTrue(self.custom_question_filter.has_changed)

    def test_apply_custom_question_filter_with_wrong_url_parameter(self):
        features_codes = ['false']

        result = self.custom_question_filter.apply_filter(features_codes)

        self.assertIsNone(result)
        self.assertFalse(self.custom_question_filter.value)
        self.assertTrue(self.custom_question_filter.has_changed)

    def test_apply_custom_question_filter_same_value(self):
        self.custom_question_filter.value = True
        features_codes = ['CQ']

        self.custom_question_filter.apply_filter(features_codes)

        self.assertFalse(self.custom_question_filter.has_changed)

    def test_custom_question_filter_info_with_option_selected(self):
        self.custom_question_filter.value = True

        expected_join_query = ['INNER JOIN eb.questions q ON q.asset = dw_event.event_id']
        self.assertEqual(self.custom_question_filter.get_join_query(), expected_join_query)
        self.assertEqual(self.custom_question_filter.get_where_query(), '')

    def test_custom_question_filter_info_without_option_selected(self):
        self.custom_question_filter.value = False
        self.assertEqual(self.custom_question_filter.get_join_query(), [''])
        self.assertEqual(self.custom_question_filter.get_where_query(), '')

from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.filters import OrganizerFilter


class TestOrganizerFilter(TestCase):

    def setUp(self):
        self.organizer_filter = OrganizerFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_organizer_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='Hernan    ')

        self.organizer_filter.apply_filter(self.mock_request)

        self.assertEqual(self.organizer_filter.value, 'Hernan')
        self.assertTrue(self.organizer_filter.has_changed)

    def test_not_apply_organizer_filter(self):
        self.mock_request.GET.get = MagicMock(return_value=' ')

        self.organizer_filter.apply_filter(self.mock_request)

        self.assertFalse(self.organizer_filter.has_changed)
        self.assertIsNone(self.organizer_filter.value)

    def test_apply_organizer_filter_same_value(self):
        self.organizer_filter.value = 'Casciari'
        self.mock_request.GET.get = MagicMock(return_value='Casciari')

        self.organizer_filter.apply_filter(self.mock_request)

        self.assertFalse(self.organizer_filter.has_changed)

    def test_organizer_filter_info_with_organizer_selected(self):
        expected_result ="""
             AND (
                LOWER(dw_organizer.organizer_name) LIKE '%hernan casciari%' 
                OR LOWER(dw_org.organization_name) LIKE '%hernan casciari%'
            )
            """
        self.organizer_filter.value = "Hernan Casciari"

        self.assertEqual(self.organizer_filter.get_join_query(), [''])
        self.assertEqual(self.organizer_filter.get_where_query(), expected_result)

    def test_organizer_filter_info_without_organizer_selected(self):

        self.organizer_filter.value = None

        self.assertEqual(self.organizer_filter.get_join_query(), [''])
        self.assertEqual(self.organizer_filter.get_where_query(), '')

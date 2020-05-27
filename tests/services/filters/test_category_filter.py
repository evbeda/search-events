from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.models import Category
from search_events_app.filters import CategoryFilter


class TestCategoryFilter(TestCase):

    def setUp(self):
        self.category_filter = CategoryFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_category_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='FD')

        self.category_filter.apply_filter(self.mock_request)

        self.assertEqual(self.category_filter.value.name, 'Food & Drink')
        self.assertTrue(self.category_filter.has_changed)

    def test_not_apply_category_filter(self):
        self.category_filter.apply_filter(self.mock_request)

        self.assertFalse(self.category_filter.has_changed)
        self.assertIsNone(self.category_filter.value)

    def test_apply_category_filter_with_wrong_data(self):
        self.mock_request.GET.get = MagicMock(return_value='Incorrect Category')

        self.category_filter.apply_filter(self.mock_request)

        self.assertFalse(self.category_filter.has_changed)
        self.assertIsNone(self.category_filter.value)

    def test_apply_category_filter_same_value(self):
        category = Category.objects.get(code='FD')
        self.category_filter.value = category
        self.mock_request.GET.get = MagicMock(return_value='FD')

        self.category_filter.apply_filter(self.mock_request)

        self.assertFalse(self.category_filter.has_changed)

    def test_category_filter_info_with_category_selected(self):

        self.category_filter.value = Category(name='Fashion & Beauty', code='FB')

        self.assertEqual(self.category_filter.get_join_query(), [''])
        self.assertEqual(self.category_filter.get_where_query(), " AND dw_cat.event_category_desc = 'Fashion & Beauty' ")

    def test_category_filter_info_without_category_selected(self):

        self.category_filter.value = None

        self.assertEqual(self.category_filter.get_join_query(), [''])
        self.assertEqual(self.category_filter.get_where_query(), '')

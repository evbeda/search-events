from unittest.mock import patch

from django.test import TestCase
from django.db.models import Q

from search_events_app.models import Category


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.get(code='FD')

    def test_category_basic_info(self):
        self.assertEqual(self.category.name, 'Food & Drink')
        self.assertEqual(self.category.code, 'FD')

    def test_category_str(self):
        self.assertEqual(self.category.__str__(), 'Food & Drink')

    def test_verbose_name_plural(self):
        verbose_name_plural = self.category._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Categories')

    @patch.object(Category.objects, 'all')
    def test_get_context(self, mock_objects):
        categories = Category.objects.filter(Q(code='CC') | Q(code='FB'))
        mock_objects.return_value = categories

        expected_result = {
            'categories': [
                {
                    'code': 'CC',
                    'name': 'Community & Culture',
                },
                {
                    'code': 'FB',
                    'name': 'Fashion & Beauty',
                },
            ]
        }

        result = Category.get_context()

        self.assertEqual(result, expected_result)

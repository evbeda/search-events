from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.services.filters.language_filter import LanguageFilter
from search_events_app.models.language import Language


class TestLanguageFilter(TestCase):

    def setUp(self):
        self.language = Language.objects.create(name='German', code='de')
        self.language_filter = LanguageFilter()
        self.mock_request = MagicMock()
        self.mock_request.GET = MagicMock()

    def test_apply_language_filter(self):
        self.mock_request.GET.get = MagicMock(return_value='de')

        self.language_filter.apply_filter(self.mock_request)

        self.assertEqual(self.language_filter.value.name, "German")
        self.assertTrue(self.language_filter.has_changed)

    def test_not_apply_language_filter(self):
        self.language_filter.apply_filter(self.mock_request)

        self.assertFalse(self.language_filter.has_changed)
        self.assertIsNone(self.language_filter.value)

    def test_apply_language_filter_with_wrong_data(self):
        self.mock_request.GET.get = MagicMock(return_value='English')

        self.language_filter.apply_filter(self.mock_request)

        self.assertFalse(self.language_filter.has_changed)
        self.assertIsNone(self.language_filter.value)

    def test_apply_language_filter_same_value(self):
        self.language_filter.value = self.language
        self.mock_request.GET.get = MagicMock(return_value='de')

        self.language_filter.apply_filter(self.mock_request)

        self.assertFalse(self.language_filter.has_changed)

    def test_language_filter_info(self):
        self.mock_request.GET.get = MagicMock(return_value='de')

        self.language_filter.apply_filter(self.mock_request)

        self.assertEqual(self.language_filter.get_key(), "language")
        self.assertEqual(self.language_filter.get_value(), "German")
        self.assertEqual(self.language_filter.get_type(), "search")
        self.assertEqual(self.language_filter.get_request_value(), {
            'languages': ["de"]
        })

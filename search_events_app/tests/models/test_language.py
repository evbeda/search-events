from unittest.mock import (
	MagicMock,
	patch,
)

from django.test import TestCase
from django.db.models import Q

from search_events_app.models.language import Language


class TestLanguage(TestCase):

    def setUp(self):
        self.language = Language.objects.get(name='English')

    def test_language_basic_info(self):
        self.assertEqual(self.language.name, 'English')
        self.assertEqual(self.language.code, 'en')

    def test_language_str(self):
        self.assertEqual(self.language.__str__(), 'English')

    @patch.object(Language.objects, 'order_by')
    def test_get_context(self, mock_objects):
        languages = Language.objects.filter(Q(name='Spanish') | Q(name='German'))
        mock_objects.return_value = languages
        
        expected_result = {
            'languages': [
                {
                    'code': 'de',
                    'name': 'German',
                },
                {
                    'code': 'es',
                    'name': 'Spanish',
                },
            ]
        }

        result = Language.get_context()

        self.assertEqual(result, expected_result)

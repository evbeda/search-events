from unittest.mock import (
	MagicMock,
	patch,
)

from django.test import TestCase

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
        languages = [
			Language(name='Spanish', code='es'),
			Language(name='German', code='de')
		]
        
        mock_objects.return_value = languages
        
        expected_result = {
            'languages': [
                {
                    'code': 'es',
                    'name': 'Spanish'
                },
                {
                    'code': 'de',
                    'name': 'German'
                }
            ]
        }

        result = Language.get_context()

        self.assertEqual(result, expected_result)
    
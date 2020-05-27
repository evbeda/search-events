from unittest.mock import patch

from django.test import TestCase
from django.db.models import Q

from search_events_app.models import Format


class TestFormat(TestCase):

    def setUp(self):
        self.format = Format.objects.get(code='GC')

    def test_language_basic_info(self):
        self.assertEqual(self.format.name, 'Game or Competition')

    def test_language_str(self):
        self.assertEqual(self.format.__str__(), 'Game or Competition')

    @patch.object(Format.objects, 'all')
    def test_get_context(self, mock_objects):
        formats = Format.objects.filter(Q(code='GC') | Q(code='Tr'))
        mock_objects.return_value = formats
        
        expected_result = {
            'formats': [
                {
                    'code': 'GC',
                    'name': 'Game or Competition',
                },
                {
                    'code': 'Tr',
                    'name': 'Tour',
                },
            ]
        }

        result = Format.get_context()

        self.assertEqual(result, expected_result)

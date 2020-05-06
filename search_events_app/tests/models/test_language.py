from django.test import TestCase

from search_events_app.models.language import Language


class TestLanguage(TestCase):

    def setUp(self):
        self.language = Language.objects.create(name='English', code='EN')

    def test_language_basic_info(self):
        self.assertEqual(self.language.name, 'English')
        self.assertEqual(self.language.code, 'EN')

    def test_language_str(self):
        self.assertEqual(self.language.__str__(), 'English')

from django.test import TestCase

from search_events_app.models.language import Language


class TestCountry(TestCase):

    def setUp(self):
        self.language = Language.objects.create(name="England", code="EN")

    def test_language_basic_info(self):
        self.assertEqual(self.language.name, "England")
        self.assertEqual(self.language.code, "EN")

    def test_language_str(self):
        self.assertEqual(self.language.__str__(), "England")

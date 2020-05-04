from django.test import TestCase

from search_events_app.models.country import Country


class TestCountry(TestCase):

    def setUp(self):
        self.country = Country.objects.create(label="Argentina", code="AR",
        eventbrite_id="1234")

    def test_country_basic_info(self):
        self.assertEqual(self.country.name, "Argentina")
        self.assertEqual(self.country.alpha_2_code, "AR")
        self.assertEqual(self.country.eventbrite_id, "1234")

    def test_country_str(self):
        self.assertEqual(self.country.__str__(), "Argentina")

from unittest.mock import patch

from django.test import TestCase
from django.db.models import Q

from search_events_app.models import City


class TestCity(TestCase):

    def setUp(self):
        self.city_mendoza = City.objects.get(name='Mendoza', country='AR')
        self.city_california = City.objects.get(name='California', country='US')

    def test_city_basic_info(self):
        self.assertEqual(self.city_california.name, 'California')
        self.assertEqual(self.city_california.code, 'CA')
        self.assertEqual(self.city_california.country, 'US')

    def test_city_basic_info_without_code(self):
        self.assertEqual(self.city_mendoza.name, 'Mendoza')
        self.assertEqual(self.city_mendoza.code, '')
        self.assertEqual(self.city_mendoza.country, 'AR')

    def test_city_mendoza_str(self):
        self.assertEqual(self.city_mendoza.__str__(), 'Mendoza')

    def test_verbose_name_plural(self):
        verbose_name_plural = self.city_mendoza._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Cities')

from unittest.mock import (
	MagicMock,
	patch
)
from django.test import Client

from django.test import TestCase

from search_events_app.models.country import Country
from search_events_app.views import EventListView


class TestEventListView(TestCase):

	@patch.object(
		Country,
		"objects"
	)
	def test_get_context_data(self, mock_objects):
		self.client = Client()
		countries = [
			Country(name="Argentina", alpha2Code="AR", alpha3Code="ARG"),
			Country(name="Spain", alpha2Code="ES", alpha3Code="ESP")
		]
		mock_objects.all = MagicMock(return_value=countries)
		expected_result = [
			{
				'alpha2Code': "AR",
				'name': "Argentina"
			},
			{
				'alpha2Code': "ES",
				'name': "Spain"
			}
		]
		kwargs = {
			"object_list": []
		}

		result = EventListView().get_context_data(**kwargs)

		self.assertEqual(result["countries"], expected_result)


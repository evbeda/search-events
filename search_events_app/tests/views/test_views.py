from unittest.mock import (
	MagicMock,
	patch
)
from django.test import Client

from django.test import TestCase

from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.services.api_service import ApiService
from search_events_app.services.filter_manager import FilterManager
from search_events_app.services.state_manager import StateManager
from search_events_app.views import EventListView


class TestEventListView(TestCase):

	def setUp(self):
		self.events = [Event(name="Evento1", url="www.google.com")]
		StateManager.reset_events()

	@patch.object(
		Country,
		"objects"
	)
	def test_get_context_data(self, mock_objects):
		self.client = Client()
		countries = [
			Country(label="Argentina", code="AR", eventbrite_id="1234"),
			Country(label="Spain", code="ES", eventbrite_id="4567")
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

	@patch.object(
		FilterManager,
		"apply_filters"
	)
	@patch.object(
		FilterManager,
		"filter_has_changed",
		return_value=False
	)
	def test_get_queryset_with_cached_events_and_filter_without_changes(self, mock_has_changed, mock_apply_filters):
		StateManager.set_events(self.events)
		view = EventListView()
		view.request = MagicMock()
		result = view.get_queryset()
		self.assertEqual(result, self.events)

	@patch.object(
		FilterManager,
		"apply_filters"
	)
	@patch.object(
		FilterManager,
		"filter_has_changed",
		return_value=True
	)
	def test_get_queryset_without_cached_events_and_filter_with_changes(self, mock_has_changed, mock_apply_filters):
		with patch.object(ApiService, 'get_events', return_value= self.events):
			view = EventListView()
			view.request = MagicMock()
			result = view.get_queryset()
			self.assertEqual(result, self.events)

	@patch.object(
		FilterManager,
		"apply_filters"
	)
	@patch.object(
		FilterManager,
		"filter_has_changed",
		return_value=True
	)
	def test_get_queryset_with_cached_events_and_filter_with_changes(self, mock_has_changed, mock_apply_filters):
		StateManager.set_events(self.events)
		with patch.object(ApiService, 'get_events', return_value= self.events):
			view = EventListView()
			view.request = MagicMock()
			result = view.get_queryset()
			self.assertEqual(result, self.events)

	@patch.object(
		FilterManager,
		"apply_filters"
	)
	@patch.object(
		FilterManager,
		"filter_has_changed",
		return_value=False
	)
	def test_get_queryset_without_cached_events_and_filter_without_changes(self, mock_has_changed, mock_apply_filters):
		with patch.object(ApiService, 'get_events', return_value=self.events):
			view = EventListView()
			view.request = MagicMock()
			result = view.get_queryset()
			self.assertEqual(result, self.events)

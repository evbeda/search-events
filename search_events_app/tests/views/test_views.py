from unittest.mock import (
	MagicMock,
	patch,
)

from django.test import (
	TestCase,
	Client,
)

from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.models.language import Language
from search_events_app.services.db.db_service import DBService
from search_events_app.services.filter_manager import FilterManager
from search_events_app.services.state_manager import StateManager
from search_events_app.views import EventListView
from search_events_app.exceptions.okta_error import OktaCredentialError
from search_events_app.exceptions.presto_error import PrestoError


class TestEventListView(TestCase):

	def setUp(self):
		self.events = [Event(name='Evento1', url='www.google.com')]
		StateManager.reset_events()

	@patch.object(Country, 'objects')
	def test_get_context_data_countries(self, mock_objects):
		self.client = Client()
		countries = [
			Country(label='Argentina', code='AR', eventbrite_id='1234'),
			Country(label='Spain', code='ES', eventbrite_id='4567')
		]
		mock_objects.all = MagicMock(return_value=countries)
		expected_result = [
			{
				'alpha2Code': 'AR',
				'name': 'Argentina'
			},
			{
				'alpha2Code': 'ES',
				'name': 'Spain'
			}
		]
		kwargs = {
			'object_list': []
		}

		result = EventListView().get_context_data(**kwargs)

		self.assertEqual(result['countries'], expected_result)

	@patch.object(Language, 'objects')
	def test_get_context_data_languages(self, mock_objects):
		self.client = Client()
		languages = [
			Language(name='Spanish', code='es'),
			Language(name='German', code='de')
		]
		mock_objects.order_by = MagicMock(return_value=languages)
		expected_result = [
			{
				'code': 'es',
				'name': 'Spanish'
			},
			{
				'code': 'de',
				'name': 'German'
			}
		]
		kwargs = {
			'object_list': []
		}

		result = EventListView().get_context_data(**kwargs)

		self.assertEqual(result['languages'], expected_result)

	@patch.object(FilterManager, 'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=False)
	def test_get_queryset_with_cached_events_and_filter_without_changes(self, mock_has_changed, mock_apply_filters):
		StateManager.set_events(self.events)
		view = EventListView()
		view.request = MagicMock()
		result = view.get_queryset()
		self.assertEqual(result, self.events)

	@patch.object(StateManager, 'set_events')
	@patch.object(FilterManager, 'get_list_dto_db_service_filter')
	@patch.object(FilterManager,'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=True)
	def test_get_queryset_without_cached_events_and_filter_with_changes(
			self,
			mock_has_changed,
			mock_apply_filters,
			mock_get_list_dto,
			mock_set_events
	):
		with patch.object(DBService, 'get_events', return_value=self.events):
			view = EventListView()
			view.request = MagicMock()
			result = view.get_queryset()
			set_events_count = mock_set_events.call_count
			get_dto_list_count = mock_get_list_dto.call_count
			self.assertEqual(result, self.events)
			self.assertEqual(set_events_count, 1)
			self.assertEqual(get_dto_list_count, 1)

	@patch.object(StateManager, 'set_events')
	@patch.object(FilterManager, 'get_list_dto_db_service_filter')
	@patch.object(FilterManager, 'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=True)
	def test_get_queryset_with_cached_events_and_filter_with_changes(
		self,
		mock_has_changed,
		mock_apply_filters,
		mock_get_list_dto,
		mock_set_events
	):
		StateManager.events = self.events
		with patch.object(DBService, 'get_events', return_value=self.events):
			view = EventListView()
			view.request = MagicMock()
			result = view.get_queryset()
			set_events_count = mock_set_events.call_count
			get_dto_list_count = mock_get_list_dto.call_count
			self.assertEqual(result, self.events)
			self.assertEqual(set_events_count, 1)
			self.assertEqual(get_dto_list_count, 1)

	@patch.object(StateManager, 'set_events')
	@patch.object(FilterManager, 'get_list_dto_db_service_filter')
	@patch.object(FilterManager, 'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=False)
	def test_get_queryset_without_cached_events_and_filter_without_changes(
		self,
		mock_has_changed,
		mock_apply_filters,
		mock_get_list_dto,
		mock_set_events
	):
		with patch.object(DBService, 'get_events', return_value=self.events):
			view = EventListView()
			view.request = MagicMock()
			result = view.get_queryset()
			set_events_count = mock_set_events.call_count
			get_dto_list_count = mock_get_list_dto.call_count
			self.assertEqual(result, self.events)
			self.assertEqual(set_events_count, 1)
			self.assertEqual(get_dto_list_count, 1)
	
	@patch("search_events_app.views.ListView.get")
	def test_get(self, mock_super_get):
		view = EventListView()
		mock_request = MagicMock()
		result_super = MagicMock()
		mock_super_get.return_value = result_super

		result = view.get(mock_request)

		self.assertEqual(result, result_super)
	
	@patch("search_events_app.views.ListView.get")
	def test_get_redirects_login(self, mock_super_get):
		view = EventListView()
		mock_request = MagicMock()
		mock_super_get.side_effect = Exception()
		response = view.get(mock_request)
		response.client = Client()
		
		self.assertRedirects(response,'/login')

	@patch("search_events_app.views.render")
	@patch("search_events_app.views.ListView.get")
	def test_get_render_error(self, mock_super_get, mock_render):
		view = EventListView()
		mock_request = MagicMock()
		presto_error = PrestoError(Exception())
		mock_super_get.side_effect = presto_error
		
		view.get(mock_request)
		count_calls = mock_render.call_count
		args_calls = mock_render.call_args[0]

		self.assertEqual(count_calls, 1)
		self.assertEqual(args_calls[1], 'event_list.html')
		self.assertEqual(args_calls[2]['error'], presto_error.message)

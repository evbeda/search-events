from unittest.mock import (
	MagicMock,
	patch,
)

from django.test import (
	TestCase,
	Client,
)

from search_events_app.models import (
	Country,
	Event,
	Feature,
	Language,
)
from search_events_app.services.db.db_service import DBService
from search_events_app.services.db.db_connection_manager import ConnectionManager
from search_events_app.services import (
	FilterManager,
	StateManager,
)
from search_events_app.views import EventListView
from search_events_app.exceptions import PrestoError


class TestEventListView(TestCase):

	def setUp(self):
		self.events = [Event(name='Evento1', url='www.google.com')]
		StateManager.reset_events()

	@patch.object(Country,'get_context')
	@patch.object(Language, 'get_context')
	@patch.object(Feature, 'get_context')
	def test_get_context_data(self, mock_features, mock_languages, mock_countries):
		arr_features = [
				{
					'code': 'RS',
					'name': 'Reserved Seating',
				},
			]
		arr_languages = [
				{
					'code': 'de',
					'name': 'German',
				},
		]
		arr_countries = [
				{
					'alpha2Code': 'PE',
					'name': 'Peru',
				},
		]
		mock_features.return_value = {
			'features': arr_features
		}
		mock_languages.return_value = {
			'languages': arr_languages
		}
		mock_countries.return_value = {
			'countries': arr_countries
		}
		view = EventListView()
		kwargs = {
			'object_list': []
		}
		result = view.get_context_data(**kwargs)
		self.assertEqual(result['features'], arr_features)
		self.assertEqual(result['languages'], arr_languages)
		self.assertEqual(result['countries'], arr_countries)

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

	@patch("search_events_app.views.event_list_view.ListView.get")
	def test_get(self, mock_super_get):
		view = EventListView()
		mock_request = MagicMock()
		result_super = MagicMock()
		mock_super_get.return_value = result_super

		result = view.get(mock_request)

		self.assertEqual(result, result_super)

	@patch("search_events_app.views.event_list_view.ListView.get")
	def test_get_with_exception_redirects_login(self, mock_super_get):
		view = EventListView()
		mock_request = MagicMock()
		mock_super_get.side_effect = Exception()
		response = view.get(mock_request)
		response.client = Client()

		self.assertRedirects(response,'/login/')

	@patch.object(ConnectionManager, 'get_connection')
	def test_get_without_connection_redirects_login(self, mock_get_connection):
		mock_get_connection.return_value = None

		view = EventListView()
		mock_request = MagicMock()
		response = view.get(mock_request)
		response.client = Client()

		self.assertRedirects(response, '/login/')

	@patch("search_events_app.views.event_list_view.render")
	@patch("search_events_app.views.event_list_view.ListView.get")
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




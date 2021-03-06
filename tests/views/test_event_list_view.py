from unittest.mock import (
	MagicMock,
	patch,
)

from django.test import (
	TestCase,
	Client,
)

from search_events_app.factories.query_parameter_factory import QueryParameterFactory
from search_events_app.models import (
	Country,
	Event,
	Feature,
	Format,
	Language,
	Category,
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
	
	@patch.object(Category, 'get_context')
	@patch.object(Country, 'get_context')
	@patch.object(Language, 'get_context')
	@patch.object(Feature, 'get_context')
	@patch.object(Format, 'get_context')
	def test_get_context_data(self, mock_formats, mock_features, mock_languages, mock_countries, mock_categories):
		arr_formats = [
				{
					'code': 'ST',
					'name': 'Seminar or Talk',
				},
			]
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
		arr_categories = [
			{
				'code': 'FD',
				'name': 'Food & Drink',
			}
		]
		mock_formats.return_value = {
			'formats': arr_formats
		}
		mock_features.return_value = {
			'features': arr_features
		}
		mock_languages.return_value = {
			'languages': arr_languages
		}
		mock_countries.return_value = {
			'countries': arr_countries
		}
		mock_categories.return_value = {
			'categories': arr_categories
		}
		view = EventListView()
		kwargs = {
			'object_list': []
		}
		view.request = MagicMock()
		view.request.path = 'SpecificEvent'

		result = view.get_context_data(**kwargs)
		self.assertEqual(result['formats'], arr_formats)
		self.assertEqual(result['features'], arr_features)
		self.assertEqual(result['languages'], arr_languages)
		self.assertEqual(result['countries'], arr_countries)
		self.assertEqual(result['categories'], arr_categories)
		self.assertTrue(result['specific_event'])

	@patch.object(FilterManager, 'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=False)
	def test_get_queryset_with_cached_events_and_filter_without_changes(self, mock_has_changed, mock_apply_filters):
		StateManager.set_events(self.events)
		StateManager.url = 'find_features'
		view = EventListView()
		view.request = MagicMock()
		view.request.path = 'find_features'
		view.request.GET = {'country': '', 'format': ''}
		result = view.get_queryset()
		self.assertEqual(result, self.events)

	@patch.object(QueryParameterFactory, 'get_query_parameters')
	@patch.object(StateManager, 'set_events')
	@patch.object(FilterManager, 'get_list_dto_db_service_filter')
	@patch.object(FilterManager, 'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=True)
	def test_get_queryset_without_cached_events_and_filter_with_changes(
			self,
			mock_has_changed,
			mock_apply_filters,
			mock_get_list_dto,
			mock_set_events,
			mock_get_query_parameters
	):
		with patch.object(DBService, 'get_events', return_value=self.events):
			view = EventListView()
			view.request = MagicMock()
			view.request.GET = {'country': '', 'format': ''}
			result = view.get_queryset()
			set_events_count = mock_set_events.call_count
			get_dto_list_count = mock_get_list_dto.call_count
			get_query_parameters_count = mock_get_query_parameters.call_count
			self.assertEqual(result, self.events)
			self.assertEqual(set_events_count, 1)
			self.assertEqual(get_dto_list_count, 1)
			self.assertEqual(get_query_parameters_count, 1)

	@patch.object(QueryParameterFactory, 'get_query_parameters')
	@patch.object(StateManager, 'set_events')
	@patch.object(FilterManager, 'get_list_dto_db_service_filter')
	@patch.object(FilterManager, 'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=True)
	def test_get_queryset_with_cached_events_and_filter_with_changes(
		self,
		mock_has_changed,
		mock_apply_filters,
		mock_get_list_dto,
		mock_set_events,
		mock_get_query_parameters
	):
		StateManager.events = self.events
		with patch.object(DBService, 'get_events', return_value=self.events):
			view = EventListView()
			view.request = MagicMock()
			view.request.GET = {'country': '', 'format': ''}
			result = view.get_queryset()
			set_events_count = mock_set_events.call_count
			get_dto_list_count = mock_get_list_dto.call_count
			get_query_parameters_count = mock_get_query_parameters.call_count
			self.assertEqual(result, self.events)
			self.assertEqual(set_events_count, 1)
			self.assertEqual(get_dto_list_count, 1)
			self.assertEqual(get_query_parameters_count, 1)

	@patch.object(QueryParameterFactory, 'get_query_parameters')
	@patch.object(StateManager, 'set_events')
	@patch.object(FilterManager, 'get_list_dto_db_service_filter')
	@patch.object(FilterManager, 'apply_filters')
	@patch.object(FilterManager, 'filter_has_changed', return_value=False)
	def test_get_queryset_without_cached_events_and_filter_without_changes(
		self,
		mock_has_changed,
		mock_apply_filters,
		mock_get_list_dto,
		mock_set_events,
		mock_get_query_parameters
	):
		with patch.object(DBService, 'get_events', return_value=self.events):
			view = EventListView()
			view.request = MagicMock()
			view.request.GET = {'country': '', 'format': ''}
			result = view.get_queryset()
			set_events_count = mock_set_events.call_count
			get_dto_list_count = mock_get_list_dto.call_count
			get_query_parameters_count = mock_get_query_parameters.call_count
			self.assertEqual(result, self.events)
			self.assertEqual(set_events_count, 1)
			self.assertEqual(get_dto_list_count, 1)
			self.assertEqual(get_query_parameters_count, 1)

	@patch("search_events_app.views.event_list_view.ListView.get")
	@patch.object(DBService, 'is_connected')
	def test_get(self, mock_is_connected, mock_super_get):
		mock_is_connected.return_value = True
		view = EventListView()
		mock_request = MagicMock()
		result_super = MagicMock()
		mock_super_get.return_value = result_super

		result = view.get(mock_request)

		self.assertEqual(result, result_super)

	@patch.object(DBService, 'is_connected')
	def test_get_without_connection_redirects_login(self, mock_is_connected):
		mock_is_connected.return_value = False
		view = EventListView()
		mock_request = MagicMock()
		response = view.get(mock_request)
		response.client = Client()
		self.assertRedirects(response,'/login/')

	@patch("search_events_app.views.event_list_view.ListView.get")
	def test_get_with_exception_redirects_login(self, mock_super_get):
		view = EventListView()
		mock_request = MagicMock()
		mock_super_get.side_effect = Exception()
		response = view.get(mock_request)
		response.client = Client()

		self.assertRedirects(response,'/login/')

	@patch("search_events_app.views.event_list_view.render")
	@patch("search_events_app.views.event_list_view.ListView.get")
	@patch.object(DBService, 'is_connected')
	def test_get_render_error(self, mock_is_connected, mock_super_get, mock_render):
		mock_is_connected.return_value = True
		view = EventListView()
		mock_request = MagicMock()
		presto_error = PrestoError(Exception())
		mock_super_get.side_effect = presto_error

		view.get(mock_request)
		count_calls = mock_render.call_count
		args_calls = mock_render.call_args[0]

		self.assertEqual(count_calls, 1)
		self.assertEqual(args_calls[1], 'find_feature.html')
		self.assertEqual(args_calls[2]['error'], presto_error.message)

	def test_is_from_login_true(self):
		view = EventListView()
		view.request = MagicMock()
		view.request.GET = {}

		self.assertEqual(view.is_from_login(), True)

	def test_is_from_login_false(self):
		view = EventListView()
		view.request = MagicMock()
		view.request.GET = {'country': '', 'format': ''}

		self.assertEqual(view.is_from_login(), False)

from unittest.mock import patch, MagicMock

from django.test import TestCase

from search_events_app.services.db.db_connection_manager import ConnectionManager, PrestoError


class TestDbConnectionManager(TestCase):

	@patch(
		'search_events_app.services.db.db_connection_manager.presto.connect'
	)
	def test_connect_without_previous_connection(self, mock_connect):
		ConnectionManager.connection = None
		ConnectionManager.connect()
		count = mock_connect.call_count
		self.assertEqual(count, 1)

	@patch(
		'search_events_app.services.db.db_connection_manager.presto.connect'
	)
	def test_connect_with_previous_connection(self, mock_connect):
		ConnectionManager.connection = MagicMock()
		ConnectionManager.connect()
		count = mock_connect.call_count
		self.assertEqual(count, 0)

	@patch(
		'search_events_app.services.db.db_connection_manager.presto.connect',
	)
	def test_connect_raise_exception(self, mock_connect):
		exception = Exception('Test')
		exception.args = [{'message': 'Test'},]
		mock_connect.side_effect = exception
		ConnectionManager.connection = None
		with self.assertRaises(PrestoError):
			ConnectionManager.connect()


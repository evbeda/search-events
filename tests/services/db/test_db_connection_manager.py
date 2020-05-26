from unittest.mock import patch, MagicMock

from django.test import TestCase

from search_events_app.services.db.db_connection_manager import ConnectionManager


class TestDbConnectionManager(TestCase):

	@patch('search_events_app.services.db.db_connection_manager.presto.connect')
	def test_connect_without_previous_connection(self, mock_connect):
		ConnectionManager.connection = None
		username = 'Usuario'
		password_okta = 'Contraseña'
		ConnectionManager.connect(username, password_okta)
		count = mock_connect.call_count
		self.assertEqual(count, 1)
	
	@patch('search_events_app.services.db.db_connection_manager.presto.connect')
	def test_connect_with_previous_connection(self, mock_connect):
		ConnectionManager.connection = MagicMock()
		ConnectionManager.connection.close = MagicMock()
		count = ConnectionManager.connection.close
		
		ConnectionManager.connect('username', 'password_okta')
		
		self.assertEqual(count.call_count, 1)
	
	@patch('search_events_app.services.db.db_connection_manager.presto.connect')
	def test_get_connection_with_previous_connection(self, mock_connect):
		ConnectionManager.connection = MagicMock()
		ConnectionManager.get_connection()
		count = mock_connect.call_count
		self.assertEqual(count, 0)

	def test_disconnect(self):
		ConnectionManager.disconnect()
		
		connection = ConnectionManager.get_connection()

		self.assertIsNone(connection)


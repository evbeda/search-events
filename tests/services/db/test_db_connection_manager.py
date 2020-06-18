import datetime
from unittest.mock import patch, MagicMock

from django.test import TestCase

from search_events_app.services.db.db_connection_manager import ConnectionManager


class TestDbConnectionManager(TestCase):

	def setUp(self):
		self.connection = MagicMock()
		self.date = MagicMock()
		self.connection.cursor = MagicMock(return_value='Connection test')
		self.connections = {
			'12345': {
				'connection': self.connection,
				'date': self.date,
			},
			'67890': {
				'connection': self.connection,
				'date': self.date,
			},
		}

	@patch('search_events_app.services.db.db_connection_manager.presto.connect')
	def test_connect(self, mock_connect):
		connection_object = MagicMock()
		connection_object.cursor = MagicMock(return_value='Connection test')
		mock_connect.return_value = connection_object
		ConnectionManager.connections = {}
		username = 'Usuario'
		password_okta = 'Contraseña'
		session = MagicMock()
		session.session_key = '45678'

		result = ConnectionManager.connect(username, password_okta, session)
		self.assertEquals(result, 'Connection test')
		self.assertEquals(len(ConnectionManager.connections.keys()), 1)
	
	def test_get_connection_without_previous_connection(self):
		ConnectionManager.connections = self.connections
		session = MagicMock()
		session.session_key = '44444'
		result = ConnectionManager.get_connection(session)

		self.assertIsNone(result)
	
	def test_get_connection_with_previous_connection(self):
		ConnectionManager.connections = self.connections
		session_key = '12345'
		result = ConnectionManager.get_connection(session_key)
		
		self.assertEquals(result, 'Connection test')

	def test_disconnect(self):
		ConnectionManager.connections = self.connections
		session = MagicMock()
		session.session_key = '12345'
		ConnectionManager.disconnect(session)
		
		expected_result = {
			'67890': {
				'connection': self.connection,
				'date': self.date,
			}
		}

		self.assertEquals(ConnectionManager.connections, expected_result)

	def test_check_and_clean_connections_under_limit(self):
		ConnectionManager.connections = self.connections
		expected_result = self.connections

		ConnectionManager.check_and_clean_connections()

		self.assertEquals(ConnectionManager.connections, expected_result)

	def test_check_and_clean_connections_over_limit(self):
		ConnectionManager.connections = {
			str(i): {
				'connection': self.connection,
				'date': datetime.date.today()-datetime.timedelta(days=i),
			} for i in range(60)
		}
		expected_result = {
			'0': {
				'connection': self.connection,
				'date': datetime.date.today(),
			},
			'1': {
				'connection': self.connection,
				'date': datetime.date.today()-datetime.timedelta(days=1),
			},
		}
		
		ConnectionManager.check_and_clean_connections()

		self.assertEquals(ConnectionManager.connections, expected_result)

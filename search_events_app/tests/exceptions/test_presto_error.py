from unittest.mock import patch

from django.test import TestCase

from search_events_app.services.db.db_connection_manager import  PrestoError


class TestPrestoError(TestCase):

	@patch.object(
		PrestoError,
		'get_message'
	)
	def test_create_presto_error(self, mock_get_message):
		result = PrestoError('Test')
		count = mock_get_message.call_count
		self.assertEqual(1, count)
		self.assertIsNotNone(result.args)

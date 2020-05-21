from requests.exceptions import (
	SSLError,
	ConnectionError,
)

from django.test import TestCase

from search_events_app.exceptions import PrestoError


class TestPrestoError(TestCase):

	def test_create_presto_error_due_to_connection_error(self):
		result = PrestoError(ConnectionError())
		self.assertEqual(result.message, 'Make sure you are connected to the VPN!')

	def test_create_presto_error_due_to_ssl_error(self):
		result = PrestoError(SSLError())
		self.assertEqual(result.message, 'Update your certificate from this <a href="https://docs.evbhome.com/intro/self_signed_certs.html">link</a>.')

	def test_create_presto_error_due_to_os_error(self):
		result = PrestoError(OSError())
		expected_message = 'Download the certificate '
		expected_message += '<a href="https://docs.evbhome.com/intro/self_signed_certs.html">link</a> '
		expected_message += 'and update the path of your environment variable.'
		self.assertEqual(result.message, expected_message)

	def test_create_presto_error_due_to_unexpected_error(self):
		result = PrestoError(Exception())
		self.assertEqual(result.message, 'There was an unexpected error with Presto')

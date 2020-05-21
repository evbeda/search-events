from django.test import TestCase

from search_events_app.exceptions import OktaCredentialError


class TestOktaError(TestCase):

	def test_okta_error(self):
		result = OktaCredentialError()
		self.assertEqual(result.message, 'Invalid Okta user or password')

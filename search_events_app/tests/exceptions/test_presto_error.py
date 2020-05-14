from unittest.mock import patch

from django.test import TestCase

from search_events_app.services.db.db_connection_manager import  PrestoError


class TestPrestoError(TestCase):

	def test_create_presto_error(self):
		pass

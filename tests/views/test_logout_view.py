from unittest.mock import (
    MagicMock,
    patch,
)

from django.test import (
    TestCase,
    Client,
)
from django.core.exceptions import SuspiciousOperation


from search_events_app.services.db.db_service import DBService
from search_events_app.views import logout
from search_events_app.exceptions import (
    OktaCredentialError,
    PrestoError,
)


class TestLogoutView(TestCase):

    def setUp(self):
        self.mock_request = MagicMock()

    def test_redirects_login(self):
        self.mock_request.method = 'POST'

        response = logout(self.mock_request)
        response.client = Client()
        
        self.assertRedirects(response, '/login/')

    def test_raises_exception_method_get(self):
        self.mock_request.method = 'GET'

        with self.assertRaises(SuspiciousOperation):
            logout(self.mock_request)
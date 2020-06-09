from unittest.mock import (
    MagicMock,
    patch,
)

from django.test import (
    TestCase,
    Client,
)

from search_events_app.services.db.db_service import DBService
from search_events_app.views import login
from search_events_app.exceptions import (
    OktaCredentialError,
    PrestoError,
)


class TestLoginView(TestCase):

    @patch("search_events_app.views.login_view.render")
    def test_login_render(self, mock_render):
        mock_request = MagicMock()
        mock_request.method = 'GET'

        login(mock_request)
        count_calls = mock_render.call_count
        args_calls = mock_render.call_args[0]

        self.assertEqual(count_calls, 1)
        self.assertEqual(args_calls[1], 'login.html')

    @patch.object(DBService, 'create_connection')
    def test_login_enter_credentials_without_error(self, mock_create_connection):
        mock_request = MagicMock()
        mock_request.method = 'POST'
        mock_request.POST = {
            'username': 'user',
            'password': '1234'
        }

        response = login(mock_request)
        response.client = Client()

        self.assertRedirects(response, '/FindFeature/')

    @patch("search_events_app.views.login_view.render")
    @patch.object(DBService, 'create_connection')
    def test_login_enter_credentials_with_credential_error(self, mock_create_connection, mock_render):
        okta_error = OktaCredentialError()
        mock_create_connection.side_effect = okta_error
        mock_request = MagicMock()
        mock_request.method = 'POST'
        mock_request.POST = {
            'username': 'user',
            'password': '1234'
        }

        login(mock_request)
        count_calls = mock_render.call_count
        args_calls = mock_render.call_args[0]

        self.assertEqual(count_calls, 1)
        self.assertEqual(args_calls[1], 'login.html')
        self.assertEqual(args_calls[2]['error'], okta_error.message)

    @patch("search_events_app.views.login_view.render")
    @patch.object(DBService, 'create_connection')
    def test_login_enter_credentials_with_presto_error(self, mock_create_connection, mock_render):
        presto_error = PrestoError(Exception())
        mock_create_connection.side_effect = presto_error
        mock_request = MagicMock()
        mock_request.method = 'POST'
        mock_request.POST = {
            'username': 'user',
            'password': '1234'
        }

        login(mock_request)
        count_calls = mock_render.call_count
        args_calls = mock_render.call_args[0]

        self.assertEqual(count_calls, 1)
        self.assertEqual(args_calls[1], 'login.html')
        self.assertEqual(args_calls[2]['error'], presto_error.message)

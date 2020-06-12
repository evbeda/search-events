from unittest.mock import (
    MagicMock,
    patch,
)
from pyhive.exc import OperationalError

from django.test import TestCase

from search_events_app.dto import DTODBServiceFilter
from search_events_app.services.db.db_service import DBService
from search_events_app.services.db.db_connection_manager import ConnectionManager
from search_events_app.models import Event
from search_events_app.exceptions import (
    OktaCredentialError,
    PrestoError,
)
from search_events_app.utils import FindFeatureQueryParameters


class TestDbService(TestCase):

    def setUp(self):
        self.mock_dto_filter = [DTODBServiceFilter(join_query='', where_query="AND dw_event.event_language LIKE '%en%'")]
        self.mock_db_response = [
            (
                99894936444,
                'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
                'Business & Professional',
                'Meeting or Networking Event',
                'Adam Kurtz',
                'US',
                '2020-12-16',
                'en_US'
            ),
            (
                104429836452,
                'Shawn Mendes The Virtual Tour',
                'Music',
                'Concert or Performance',
                'Mia Discenza',
                None,
                '2020-05-16',
                'en_US'
            )
        ]
        self.mock_response_processed = [
            {
                'name': 'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
                'url': 'https://www.eventbrite.com/e/99894936444',
                'language': 'en',
                'start_date': '2020-12-16',
                'category': 'Business & Professional',
                'format_': 'Meeting or Networking Event',
                'organizer': 'Adam Kurtz',
                'country': 'United States'
            },
            {
                'name': 'Shawn Mendes The Virtual Tour',
                'url': 'https://www.eventbrite.com/e/104429836452',
                'language': 'en',
                'start_date': '2020-05-16',
                'category': 'Music',
                'format_': 'Concert or Performance',
                'organizer': 'Mia Discenza',
                'country': None,
            }
        ]

    @patch.object(DBService, 'execute_query')
    @patch.object(DBService, 'format_query')
    @patch('search_events_app.services.db.db_service.process_events')
    def test_get_events(self, mock_process_events, mock_format_query, mock_execute_query):
        mock_process_events.return_value = self.mock_response_processed

        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock()
        mock_cursor.fetchall = MagicMock(return_value=self.mock_db_response)

        result = DBService.get_events(dto_filters_array=self.mock_dto_filter, query_parameters=FindFeatureQueryParameters)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Event)
        self.assertIsInstance(result[1], Event)

    @patch.object(ConnectionManager, 'get_connection')
    def test_excute_query(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock()
        mock_cursor.fetchall = MagicMock(return_value=self.mock_db_response)
        mock_connect.return_value = mock_cursor
        query = 'This is query'

        result = DBService.execute_query(query)

        self.assertEqual(len(result), 2)
        self.assertEqual(type(result), list)

    @patch.object(ConnectionManager, 'get_connection')
    def test_execute_query_wrong_okta_credentials(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock(side_effect=OperationalError())
        mock_connect.return_value = mock_cursor
        query = 'SELECT 1'

        with self.assertRaises(OktaCredentialError):
            DBService.execute_query(query)

    @patch.object(ConnectionManager, 'get_connection')
    def test_excute_query_with_presto_error(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock(side_effect=Exception())
        mock_connect.return_value = mock_cursor
        query = 'SELECT 1'

        with self.assertRaises(PrestoError):
            DBService.execute_query(query)

    def test_format_query_without_filters(self):
        expected = FindFeatureQueryParameters.columns_select + FindFeatureQueryParameters.default_tables + FindFeatureQueryParameters.constraints
        expected += FindFeatureQueryParameters.group_by + FindFeatureQueryParameters.order_by + FindFeatureQueryParameters.limit

        result = DBService.format_query([], FindFeatureQueryParameters)

        self.assertEqual(result, expected)

    def test_format_query_with_filters(self):
        where_query = FindFeatureQueryParameters.constraints + " " + "AND dw_event.event_language LIKE '%en%'"
        expected = FindFeatureQueryParameters.columns_select + FindFeatureQueryParameters.default_tables + where_query + FindFeatureQueryParameters.group_by
        expected += FindFeatureQueryParameters.order_by + FindFeatureQueryParameters.limit

        result = DBService.format_query(self.mock_dto_filter, FindFeatureQueryParameters)
        self.assertEqual(result, expected)

    def test_format_join_query_with_filters(self):
        mock_dto_filter = [DTODBServiceFilter(join_query=['INNER JOIN dw.f_ticket_merchandise_purchase f ON f.event_id = dw_event.event_id'], where_query='')]
        join_query = FindFeatureQueryParameters.default_tables + " " +  "INNER JOIN dw.f_ticket_merchandise_purchase f ON f.event_id = dw_event.event_id"
        where_query = FindFeatureQueryParameters.constraints + " "
        expected = FindFeatureQueryParameters.columns_select + join_query + where_query + FindFeatureQueryParameters.group_by
        expected += FindFeatureQueryParameters.order_by + FindFeatureQueryParameters.limit

        result = DBService.format_query(mock_dto_filter, FindFeatureQueryParameters)
        self.assertEqual(result, expected)

    @patch.object(ConnectionManager, 'connect')
    @patch.object(DBService, 'execute_query')
    def test_create_connection(self, mock_execute_query, mock_connect):
        DBService.create_connection('username', 'password')

        result_execute = mock_execute_query.call_count
        result_connect = mock_connect.call_count

        self.assertEqual(result_execute, 1)
        self.assertEqual(result_connect, 1)

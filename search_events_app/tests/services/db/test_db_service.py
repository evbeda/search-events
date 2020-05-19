from unittest.mock import (
    MagicMock,
    patch,
)
from pyhive.exc import OperationalError

from django.test import TestCase


from search_events_app.services.db.db_service import DBService
from search_events_app.dto.dto_db_service_filter import DTODBServiceFilter
from search_events_app.services.db.db_connection_manager import ConnectionManager

from search_events_app.models.event import Event
from search_events_app.exceptions.okta_error import OktaCredentialError
from search_events_app.exceptions.presto_error import PrestoError
from search_events_app.utils.queries import QueryParameter


class TestDbService(TestCase):

    def setUp(self):
        self.mock_dto_filter = [DTODBServiceFilter(join_query='', where_query=" AND dw_event.event_language LIKE '%en%'")]
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

    @patch.object(ConnectionManager, 'connect')
    @patch.object(DBService, 'format_query')
    @patch('search_events_app.services.db.db_service.process_events')
    def test_get_events_without_exception(self, mock_process_events, mock_format_query, mock_connect):
        mock_process_events.return_value = self.mock_response_processed

        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock()
        mock_cursor.fetchall = MagicMock(return_value=self.mock_db_response)
        mock_connect.return_value = mock_cursor

        result = DBService.get_events(dto_filters_array=self.mock_dto_filter)

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Event)
        self.assertIsInstance(result[1], Event)

    @patch.object(ConnectionManager, 'connect')
    @patch.object(DBService, 'format_query')
    def test_get_events_wrong_okta_credentials(self, mock_format_query, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock(side_effect=OperationalError())
        mock_connect.return_value = mock_cursor

        with self.assertRaises(OktaCredentialError):
            DBService.get_events(dto_filters_array=self.mock_dto_filter)

    @patch.object(ConnectionManager, 'connect')
    @patch.object(DBService, 'format_query')
    def test_get_events_with_presto_error(self, mock_format_query, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock(side_effect=Exception())
        mock_connect.return_value = mock_cursor

        with self.assertRaises(PrestoError):
            DBService.get_events(dto_filters_array=self.mock_dto_filter)


    def test_format_query_without_filters(self):
        expected = QueryParameter.columns_select+QueryParameter.default_tables+QueryParameter.constraints+QueryParameter.order_by+QueryParameter.limit

        result = DBService.format_query([])

        self.assertEqual(result, expected)

    def test_format_query_with_filters(self):
        where_query = QueryParameter.constraints+" AND dw_event.event_language LIKE '%en%'"
        expected = QueryParameter.columns_select+QueryParameter.default_tables+where_query+QueryParameter.order_by+QueryParameter.limit

        result = DBService.format_query(self.mock_dto_filter)

        self.assertEqual(result, expected)

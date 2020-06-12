from pyhive.exc import OperationalError

from search_events_app.services.db.db_connection_manager import ConnectionManager
from search_events_app.services.db.db_response_processor import process_events
from search_events_app.models import Event
from search_events_app.exceptions import (
    PrestoError,
    OktaCredentialError,
)


class DBService:

    @classmethod
    def execute_query(cls, query):
        try:
            cursor = ConnectionManager.get_connection()
            cursor.execute(query)
            return cursor.fetchall()
        except (OperationalError, AttributeError):
            raise OktaCredentialError()
        except Exception as e:
            raise PrestoError(e)

    @classmethod
    def format_query(cls, dto_filters_array, query_parameters):
        select_base_query = query_parameters.columns_select
        join_base_query = query_parameters.default_tables
        where_base_query = query_parameters.constraints
        group_by_base_query = query_parameters.group_by
        order_by_base_query = query_parameters.order_by
        limit = query_parameters.limit
        for dto in dto_filters_array:
            for dto_join in dto.join_query:
                join_base_query += " "+dto_join
            where_base_query += " "+dto.where_query
        query = select_base_query+join_base_query+where_base_query+group_by_base_query+order_by_base_query+limit
        return query

    @classmethod
    def get_events(cls, dto_filters_array, query_parameters):
        query = cls.format_query(dto_filters_array, query_parameters)
        result = cls.execute_query(query)
        db_events = process_events(result)
        return [Event(**db_event) for db_event in db_events]

    @classmethod
    def create_connection(cls, username, password):
        ConnectionManager.connect(username, password)
        cls.execute_query('select 1')

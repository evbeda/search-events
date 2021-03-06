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
    def execute_query(cls, query, session):
        try:
            cursor = ConnectionManager.get_connection(session.session_key)
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
            select_base_query += " "+dto.select_query
            for dto_join in dto.join_query:
                join_base_query += " "+dto_join
            where_base_query += " "+dto.where_query
            group_by_base_query += " "+dto.group_query
        query = select_base_query+join_base_query+where_base_query+group_by_base_query+order_by_base_query+limit
        return query

    @classmethod
    def get_events(cls, dto_filters_array, query_parameters, session):
        query = cls.format_query(dto_filters_array, query_parameters)
        result = cls.execute_query(query, session)
        db_events = process_events(result)
        return [Event(**db_event) for db_event in db_events]

    @classmethod
    def create_connection(cls, username, password, session):
        ConnectionManager.connect(username, password, session)
        cls.execute_query('select 1', session)

    @classmethod
    def is_connected(cls, session):
        if ConnectionManager.get_connection(session.session_key):
            return True
        else:
            return False

    @classmethod
    def disconnect(cls, session):
        ConnectionManager.disconnect(session)

from pyhive.exc import OperationalError
from search_events_app.services.db.db_connection_manager import ConnectionManager
from search_events_app.services.db.db_response_processor import process_events
from search_events_app.models.event import Event
from search_events_app.exceptions.presto_error import PrestoError
from search_events_app.exceptions.okta_error import OktaCredentialError

from search_events_app.utils.queries import QueryParameter


class DBService:

    @classmethod
    def get_events(cls, dto_filters_array):
        try:
            query = cls.format_query(dto_filters_array)
            cursor = ConnectionManager.connect()
            cursor.execute(query)
            result = cursor.fetchall()
            db_events = process_events(result)
            return [Event(**db_event) for db_event in db_events]
        except OperationalError:
            raise OktaCredentialError()
        except Exception as e:
            raise PrestoError(e)

    @classmethod
    def format_query(cls, dto_filters_array):
        select_base_query = QueryParameter.columns_select
        join_base_query = QueryParameter.default_tables
        where_base_query = QueryParameter.constraints
        group_base_query = QueryParameter.order_by
        limit = QueryParameter.limit
        for dto in dto_filters_array:
            join_base_query += dto.join_query
            where_base_query += dto.where_query
        query = select_base_query+join_base_query+where_base_query+group_base_query+limit
        return query

from search_events_app.services.db.db_connection_manager import ConnectionManager
from search_events_app.services.db.db_response_processor import process_events
from search_events_app.models.event import Event


class DBService:

    @classmethod
    def get_events(cls, dto_filters_array):
        query = cls.format_query(dto_filters_array)
        cursor = ConnectionManager.connect()
        cursor.execute(query)
        result = cursor.fetchall()
        db_events = process_events(result)
        return [Event(**db_event) for db_event in db_events]

    @classmethod
    def format_query(cls, dto_filters_array):
        select_base_query = """SELECT dw_event.event_id*1003 AS id,
       dw_event.event_title,
       dw_cat.event_category_desc,
       dw_cat.event_format_desc,
       dw_org.organization_name,
       dw_event.country_desc,
       CAST(CAST(dw_event.event_start_date AS TIMESTAMP) AS DATE) AS start_date,
       dw_event.event_language
       """
        join_base_query = """FROM dw.dim_event dw_event
INNER JOIN dw.dim_organization dw_org ON dw_event.organization_id=dw_org.organization_id
INNER JOIN dw.dim_event_category dw_cat ON dw_event.dim_event_category_id = dw_cat.dim_event_category_id
INNER JOIN dw.f_ticket_merchandise_purchase f ON f.event_id = dw_event.event_id"""
        where_base_query = """
WHERE DATE(CAST(dw_event.event_sale_end_date AS TIMESTAMP)) > now() 
    AND DATE(CAST(dw_event.event_start_date AS TIMESTAMP)) > now()
  AND dw_event.is_available = 'Y'"""
        group_base_query = """
GROUP BY dw_event.event_id,
         dw_org.organization_name,
         dw_event.event_title,
         dw_event.event_language,
         dw_event.country_desc,
         dw_cat.event_category_desc,
         dw_cat.event_format_desc,
         dw_event.event_start_date
ORDER BY SUM(f.f_item_qty) DESC
LIMIT 20
"""
        for dto in dto_filters_array:
            join_base_query += dto.join_value
            where_base_query += dto.where_value
        query = select_base_query+join_base_query+where_base_query+group_base_query
        return query

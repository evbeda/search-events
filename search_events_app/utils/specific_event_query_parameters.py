class SpecificEventsQueryParameters:
    columns_select = """
         SELECT
            DISTINCT
               dw_event.event_id*1003 AS id,
               dw_event.event_title,
               dw_cat.event_category_desc,
               dw_cat.event_format_desc,
               dw_organizer.organizer_name,
               dw_org.organization_name,
               dw_event.country_desc,
               CAST(CAST(dw_event.event_start_date AS TIMESTAMP) AS DATE) AS start_date,
               dw_event.event_language
    """

    default_tables = """ 
        FROM dw.dim_event dw_event
            LEFT JOIN (
               SELECT organizer_id,organizer_name
               FROM hive.dw.dim_organizer
            ) AS dw_organizer ON dw_event.organizer_id=dw_organizer.organizer_id
            LEFT JOIN (
               SELECT organization_id, organization_name
               FROM hive.dw.dim_organization
            ) AS dw_org ON dw_event.organization_id=dw_org.organization_id
            INNER JOIN ( 
               SELECT dim_event_category_id, event_category_desc, event_format_desc 
               FROM hive.dw.dim_event_category
            ) AS dw_cat ON dw_event.dim_event_category_id = dw_cat.dim_event_category_id
    """

    constraints = """ 
        WHERE 
           CAST(CAST(dw_event.event_start_date AS TIMESTAMP) AS DATE) >= NOW()
        """
    group_by = ''

    order_by = """ 
         ORDER BY
            CAST(CAST(dw_event.event_start_date AS TIMESTAMP) AS DATE) ASC,
            dw_event.event_id*1003,
            dw_event.event_title,
            dw_cat.event_category_desc,
            dw_cat.event_format_desc,
            dw_organizer.organizer_name,
            dw_org.organization_name,
            dw_event.country_desc,
            dw_event.event_language
    """

    limit = ' LIMIT 50'

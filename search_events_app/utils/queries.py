class QueryParameter:
    columns_select = """ 
        SELECT dw_event.event_id*1003 AS id,
            dw_event.event_title,
            dw_cat.event_category_desc,
            dw_cat.event_format_desc,
            dw_org.organization_name,
            dw_event.country_desc,
            CAST(CAST(dw_event.event_start_date AS TIMESTAMP) AS DATE) AS start_date,
            dw_event.event_language
    """
    
    default_tables = """ 
        FROM dw.dim_event dw_event
        INNER JOIN dw.dim_organization dw_org ON dw_event.organization_id=dw_org.organization_id
        INNER JOIN dw.dim_event_category dw_cat ON dw_event.dim_event_category_id = dw_cat.dim_event_category_id
    """

    constraints = """ 
        WHERE 
            DATE(CAST(dw_event.event_sale_end_date AS TIMESTAMP)) > now() + interval '1' month
            AND DATE(CAST(dw_event.event_start_date AS TIMESTAMP)) BETWEEN 
                now() + interval '1' month 
                AND now() +  interval '6' month
            AND dw_event.is_available = 'Y'
            AND dw_event.event_status = 'Live'
            AND dw_event.event_status_text_code NOT IN ('event_cancelled', 'tickets_sold_out', 'event_postponed')
        """

    order_by = """ 
        ORDER BY dw_event.event_start_date
    """

    limit = ' LIMIT 20'

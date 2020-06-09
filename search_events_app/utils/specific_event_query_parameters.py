class SpecificEventsQueryParameters:
    columns_select = """
        SELECT dw_event.event_id*1003 AS id,
            dw_event.event_title,
            dw_cat.event_category_desc,
            dw_cat.event_format_desc,
            dw_organizer.organizer_name,
            dw_org.organization_name,
            dw_event.country_desc,
            CAST(CAST(dw_event.event_start_date AS TIMESTAMP) AS DATE) AS start_date,
            dw_event.event_language,
            es.domain
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
        LEFT JOIN (
            SELECT event_id, f_item_qty, trx_type, q_order_affiliate_code
            FROM hive.dw.f_ticket_merchandise_purchase
            WHERE is_valid = 'Y'
        ) AS f ON f.event_id = dw_event.event_id
        INNER JOIN (
            SELECT event, SUM(is_donation) as donation
            FROM hive.eb.ticket_classes
            WHERE
            deleted='n'
            AND end_sales > now()
            AND (start_sales < now() OR start_sales IS NULL)
            GROUP BY event
            HAVING (SUM(quantity_total) > SUM(quantity_sold) OR SUM(quantity_total) = 0 OR SUM(is_donation) > 0)
        ) AS ts ON ts.event = dw_event.event_id
        LEFT JOIN(
            SELECT DISTINCT(es.event_id) as event, min(domain.name) as domain
            FROM hive.theme_builder.events_theme_applications as es
            INNER JOIN (
                SELECT id, owner_id
                FROM hive.theme_builder.theme_applications
                WHERE is_published=1 AND is_deleted=0
            ) as t on t.id = es.theme_application_id
            INNER JOIN(
                SELECT owner_id
                FROM hive.theme_builder.subscriptions
                WHERE (product_id=2 OR product_id=4) AND status NOT like '%canceled%'
            )AS s on s.owner_id=t.owner_id
            INNER JOIN(
                SELECT name, theme_application_id
                FROM hive.theme_builder.domains
                WHERE is_active=1 and name like '%eventbritestudio%'
            ) as domain ON domain.theme_application_id = es.theme_application_id
            GROUP by  es.event_id
        ) AS es ON es.event = dw_event.event_id
    """

    constraints = """ 
        WHERE 
            DATE(CAST(dw_event.event_sale_end_date AS TIMESTAMP)) > now() + interval '1' month
            AND DATE(CAST(dw_event.event_start_date AS TIMESTAMP)) BETWEEN 
                now() + interval '1' month 
                AND now() +  interval '6' month
            AND dw_event.is_available = 'Y'
            AND dw_event.event_status = 'Live'
            AND dw_event.is_private_event = 'N'
        """
    group_by = """
        GROUP BY dw_event.event_id,
            dw_event.event_title,
            dw_cat.event_category_desc,
            dw_cat.event_format_desc,
            dw_organizer.organizer_name,
            dw_org.organization_name,
            dw_event.country_desc,
            dw_event.event_start_date,
            dw_event.event_language,
            es.domain
    """
    order_by = """ 
        ORDER BY SUM(f.f_item_qty) DESC, dw_event.event_start_date
    """

    limit = ' LIMIT 50'

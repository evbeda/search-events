from search_events_app.filters.filter import Filter
from search_events_app.utils import FeatureCodes


class WaitlistFilter(Filter):
    def apply_filter(self, feature_codes):
        new_filter = FeatureCodes.wait_list in feature_codes
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        if self.value:
            return ["""
            INNER JOIN (
                SELECT hive.eb.waitlist.event, ticket, deleted
                FROM hive.eb.waitlist
                INNER JOIN (
                    SELECT id, deleted
                    FROM hive.eb.ticket_classes
                    WHERE (
                        quantity_sold >= quantity_total
                        AND is_donation = 0
                        AND quantity_total > 0
                        AND DATE(CAST(start_sales AS TIMESTAMP)) < NOW() - INTERVAL '1' DAY
                        AND DATE(CAST(end_sales AS TIMESTAMP)) > NOW() + INTERVAL '1' MONTH
                    )
                ) AS tc ON tc.id = hive.eb.waitlist.ticket
                WHERE tc.deleted = 'n'
            ) AS waitlist ON waitlist.event = dw_event.event_id
            """]
        return ['']

    def get_where_query(self):
        return ''

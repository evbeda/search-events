from search_events_app.filters.filter import Filter


class OrganizerFilter(Filter):

    def apply_filter(self, request):
        organizer = request.GET.get('organizer', '').strip()
        new_filter = None
        if organizer:
            new_filter = organizer

        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_where_query(self):
        if self.value:
            return 'AND ('\
                f"LOWER(dw_organizer.organizer_name) LIKE '%{self.value.lower()}%' "\
                f"OR LOWER(dw_org.organization_name) LIKE '%{self.value.lower()}%'"\
            ')'
        return ''

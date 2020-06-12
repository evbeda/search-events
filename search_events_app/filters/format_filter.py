from django.core.exceptions import ObjectDoesNotExist

from search_events_app.models import Format
from search_events_app.filters.filter import Filter


class FormatFilter(Filter):

    def apply_filter(self, request):
        format_code = request.GET.get('format')
        new_filter = None
        if format_code:
            try:
                new_filter = Format.objects.get(code=format_code)
            except ObjectDoesNotExist:
                pass
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_value(self):
        if self.value:
            return self.value.name

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return f"AND dw_cat.event_format_desc='{self.value.name}'"
        return ''

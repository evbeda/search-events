from django.core.exceptions import ObjectDoesNotExist

from search_events_app.models import Language
from search_events_app.filters.filter import Filter


class LanguageFilter(Filter):

    def apply_filter(self, request):
        language_code = request.GET.get('language')
        new_filter = None
        if language_code:
            try:
                new_filter = Language.objects.get(code=language_code)
            except ObjectDoesNotExist:
                new_filter = None
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_where_query(self):
        if self.value:
            return f"AND dw_event.event_language LIKE '%{self.value.code}_%'"
        return ''

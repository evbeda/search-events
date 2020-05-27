from django.core.exceptions import ObjectDoesNotExist

from search_events_app.filters.filter import Filter
from search_events_app.models.category import Category


class CategoryFilter(Filter):
    def apply_filter(self, request):
        category_code = request.GET.get('category', '')
        new_filter = None
        if category_code:
            try:
                new_filter = Category.objects.get(code=category_code)
            except ObjectDoesNotExist:
                new_filter = None
        self.has_changed = new_filter != self.value
        if self.has_changed:
            self.value = new_filter

    def get_join_query(self):
        return ['']

    def get_where_query(self):
        if self.value:
            return f" AND dw_cat.event_category_desc = '{self.value.name}' "
        return ''

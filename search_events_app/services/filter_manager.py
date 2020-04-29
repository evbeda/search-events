from search_events_app.services.api_service import ApiService


class FilterManager:
    latest_filter = {'country': None}

    @classmethod
    def apply_filter(cls, request):
        FilterManager.apply_field_filter(request, 'country')

    @classmethod
    def apply_field_filter(cls, request, field):
        new_filter = request.GET.get(field)
        if new_filter != cls.latest_filter.get(field):
            ApiService.clear_events()
            cls.latest_filter[field] = new_filter.lower()

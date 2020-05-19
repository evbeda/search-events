from django.views.generic.list import ListView
from django.shortcuts import render

from search_events_app.services.db.db_service import DBService
from search_events_app.models.country import Country
from search_events_app.models.language import Language
from search_events_app.services.filter_manager import FilterManager
from search_events_app.services.state_manager import StateManager


class EventListView(ListView):
    template_name = 'event_list.html'

    def get_queryset(self):
        FilterManager.apply_filters(self.request)
        if FilterManager.filter_has_changed() or not StateManager.get_last_searched_events():
            db_service_filters = FilterManager.get_list_dto_db_service_filter()
            events = DBService.get_events(db_service_filters)
            StateManager.set_events(events)
            return events
        return StateManager.get_last_searched_events()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        classes = [Country, Language]

        for c in classes:
            context.update(c.get_context())

        return context


def login(request):
    return render(request, 'login.html')

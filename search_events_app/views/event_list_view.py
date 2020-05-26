from django.views.generic.list import ListView
from django.shortcuts import (
    render,
    redirect
)

from search_events_app.services.db.db_service import DBService
from search_events_app.services.db.db_connection_manager import ConnectionManager
from search_events_app.services import (
    FilterManager,
    StateManager,
)
from search_events_app.exceptions import PrestoError
from search_events_app.models import (
    Feature,
    Country,
    Language,
)



class EventListView(ListView):
    template_name = 'event_list.html'

    def get(self, request):
        if not ConnectionManager.get_connection():
            return redirect('login')
        try:
            return super().get(request)
        except PrestoError as e:
            StateManager.reset_events()
            return render(request, 'event_list.html', {'error': e.message})
        except Exception as e:
            return redirect('login')

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

        classes = [Country, Language, Feature]

        for class_ in classes:
            context.update(class_.get_context())

        return context


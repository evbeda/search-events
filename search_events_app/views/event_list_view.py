from django.views.generic.list import ListView
from django.shortcuts import (
    render,
    redirect
)

from search_events_app.factories import (
    QueryParameterFactory,
    TemplateFactory
)
from search_events_app.services.db.db_service import DBService
from search_events_app.services.db.db_connection_manager import ConnectionManager
from search_events_app.services import (
    FilterManager,
    StateManager,
)
from search_events_app.exceptions import PrestoError
from search_events_app.models import (
    Category,
    City,
    Country,
    Currency,
    Feature,
    Format,
    Language,
)


class EventListView(ListView):

    def get(self, request):
        self.template_name = TemplateFactory.get_template(request)
        if not ConnectionManager.get_connection():
            return redirect('login')
        try:
            return super().get(request)
        except PrestoError as e:
            StateManager.reset_events()
            return render(request, 'find_feature.html', {'error': e.message})
        except Exception as e:
            return redirect('login')

    def get_queryset(self):
        if self.is_from_login():
            return []
        FilterManager.apply_filters(self.request)
        if FilterManager.filter_has_changed() or not StateManager.get_last_searched_events():
            db_service_filters = FilterManager.get_list_dto_db_service_filter()
            query_parameters = QueryParameterFactory.get_query_parameters(self.request)
            events = DBService.get_events(db_service_filters, query_parameters)
            StateManager.set_events(events)
            return events
        return StateManager.get_last_searched_events()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        classes = [Country, Language, Feature, Format, Category, Currency]

        for class_ in classes:
            context.update(class_.get_context())

        context['username'] = ConnectionManager.username

        return context

    def is_from_login(self):
        return not len(self.request.GET.keys())

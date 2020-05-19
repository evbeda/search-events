from django.views.generic.list import ListView
from django.shortcuts import (
    render,
    redirect
)
from django.urls import reverse

from search_events_app.services.db.db_service import DBService
from search_events_app.services.filter_manager import FilterManager
from search_events_app.services.state_manager import StateManager
from search_events_app.exceptions import (
    OktaCredentialError,
    PrestoError,
)
from search_events_app.models import (
    Feature,
    Country,
    Language,
)


class EventListView(ListView):
    template_name = 'event_list.html'

    def get(self, request):
        try:
            return super().get(request)
        except PrestoError as e:
            StateManager.reset_events()
            return render(request, 'event_list.html', {'error': e.message})
        except Exception as e:
            return redirect(reverse('login'))

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

        for c in classes:
            context.update(c.get_context())

        return context


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            DBService.create_connection(username, password)
            return redirect('event_list')
        except OktaCredentialError as e:
            return render(request, 'login.html', {'error': e.message})
        except PrestoError as e:
            return render(request, 'login.html', {'error': e.message})

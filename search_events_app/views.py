from django.shortcuts import render
from django.views.generic.list import ListView

from search_events_app.services import post_request_processor
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
        countries = Country.objects.all()
        languages = Language.objects.order_by('name')

        context = super().get_context_data(**kwargs)
        context['countries'] = [
            {
                'alpha2Code': country.alpha_2_code,
                'name': country.name
            } for country in countries
        ]

        context['languages'] = [
            {
                'code': language.code,
                'name': language.name
            } for language in languages
        ]
        return context

from django.shortcuts import render
from django.views.generic.list import ListView

from search_events_app.services.api_service import ApiService
from search_events_app.models.country import Country
from search_events_app.services.filter_manager import FilterManager


class EventListView(ListView):
    template_name = 'event_list.html'

    def get_queryset(self):
        FilterManager.apply_filter(self.request)
        events = ApiService().get_events(country=FilterManager.latest_filter.get('country'))
        return events

    def get_context_data(self, **kwargs):
        countries = Country.objects.all()
        context = super().get_context_data(**kwargs)
        context['countries'] = [
            {
                'alpha2Code': country.alpha_2_code,
                'name': country.name
            } for country in countries
        ]
        return context

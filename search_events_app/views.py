from django.shortcuts import render
from django.views.generic.list import ListView

from search_events_app.services.api_service import get_events
from search_events_app.models.country import Country
from search_events_app.services.filter_service import filter_events


class EventListView(ListView):
    template_name = 'event_list.html'

    def get_queryset(self):
        events = get_events()
        event = filter_events(self.request, events)
        return event

    def get_context_data(self, **kwargs):
        countries = Country.objects.all()
        context = super().get_context_data(**kwargs)
        context['countries'] = countries
        context['countries_names'] = [
            {'id': country.id, 'name': country.name} for country in countries
        ]
        return context

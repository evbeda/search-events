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

    def get_dto_filter_by_filters(self, filters):
        dict_dto = {}
        for filter_ in filters:
            dict_dto[filter_.get_key()] = filter_.get_value()

        return DTOFilter(**dict_dto)

    def get_list_dto_api_service_filter_by_filters(self, filters):
        list_dto = []
        dict_dto = {}
        for filter_ in filters:
            dict_dto['type'] = filter_.get_type()
            dict_dto['value'] = filter_.get_request_value()
            list_dto.append(DTOApiServiceFilter(**dict_dto))

        return list_dto


class DTOFilter:
    
    def __init__(self, **kwargs):
        self.country = kwargs.get('country')


class DTOApiServiceFilter:
    
    def __init__(self, **kwargs):
        self.type = kwargs.get('type')
        self.value = kwargs.get('value')

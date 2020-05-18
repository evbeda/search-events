import requests

from django.conf import settings
from search_events_app.models.event import Event
from .api_response_processor import process_events


class ApiService:

    @classmethod
    def get_events(cls, dto_filters_array):
        search_filters = [dto_filter for dto_filter in dto_filters_array if dto_filter.type == 'search']
        body_dict = cls.format_body(search_filters)
        token = '&token='+settings.TOKEN_API
        url_api = 'https://www.evbqaapi.com/v3/destination/search/?'
        url_api_expand = 'expand.destination_event=primary_organizer%2Cprimary_venue'
        response = requests.post(
            url_api+url_api_expand+token,
            json=body_dict,
            verify=False
        )
        api_events = process_events(response.json())
        return [Event(**api_event) for api_event in api_events]

    @classmethod
    def format_body(cls, dto_filters):
        base_dict = {
            'event_search': {
                'sort': 'default',
                'dates': 'current_future',
                'page_size': 40,
            }
        }
        for dto_filter in dto_filters:
            if dto_filter.value:
                base_dict['event_search'].update(dto_filter.value)
        return base_dict

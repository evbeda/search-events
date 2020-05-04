import requests
import json

from search_events_app.models.event import Event
from search_events_app.services.dummy_api import DummyApi
from .api_response_processor import process_events


class ApiService:

    @classmethod
    def get_events(cls, dto_filters_array):
        search_filters = [dto_filter for dto_filter in dto_filters_array if dto_filter.type == "search"]
        body_dict = cls.format_body(search_filters)
        response = requests.post(
            "https://www.evbqaapi.com/v3/destination/search/?" +
            "expand.destination_event=primary_organizer" +
            "%2Cprimary_venue" +
            "&token=QF44722VLJLXURKY43HZ",
            json=body_dict
        )
        api_events = process_events(response.json())
        return [Event(**api_event) for api_event in api_events]

    @classmethod
    def format_body(cls, dto_filters):
        base_dict = {
            "event_search": {
                "sort": "default",
                "dates": "current_future",
                "page_size": 20,
            }
        }
        for dto_filter in dto_filters:
            base_dict['event_search'].update(dto_filter.value)

        return base_dict



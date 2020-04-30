import requests
import json

from search_events_app.models.event import Event
from search_events_app.services.dummy_api import DummyApi
from .api_response_processor import process_events


class ApiService:

    events = None

    @classmethod
    def get_events(cls, country=None):
        if not cls.events:
            body_dict = cls.format_body(country)
            response = requests.post(
                "https://www.evbqaapi.com/v3/destination/search/?" +
                "expand.destination_event=primary_organizer" +
                "%2Cprimary_venue" +
                "&token=QF44722VLJLXURKY43HZ",
                json=body_dict
            )
            api_events = process_events(response.json())
            cls.events = [Event(**api_event) for api_event in api_events]
        return cls.events

    @classmethod
    def format_body(cls, country):
        base_dict = {
            "event_search": {
                "sort": "default",
                "page_size": 20,
            }
        }
        if country:
            base_dict['event_search']['countries'] = [country.lower()]
        return base_dict

    @classmethod
    def clear_events(cls):
        cls.events = None

import requests
import json

from search_events_app.models.event import Event
from search_events_app.services.dummy_api import DummyApi


def get_events(countries=None):
	body_dict = format_body()
	response = requests.post("https://www.evbqaapi.com/v3/destination/search/?token=QF44722VLJLXURKY43HZ", json=body_dict)
	api_events = response.json()['events']['results']
	return [Event(**api_event) for api_event in api_events]


def format_body():
	base_dict = {
		"event_search": {
			"sort": "default",
			"page_size": 100
		}
	}
	return base_dict

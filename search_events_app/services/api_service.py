import requests
import json

from search_events_app.models.event import Event
from search_events_app.services.dummy_api import DummyApi
from .api_response_processor import process_events

class ApiService:

	events = None

	def get_events(self, countries=None):
		if not ApiService.events:
			body_dict = self.format_body()
			response = requests.post(
				"https://www.evbqaapi.com/v3/destination/search/?" +
				"expand.destination_event=primary_organizer" + 
				"%2Cprimary_venue" +
				"&token=QF44722VLJLXURKY43HZ",
				json=body_dict
			)
			api_events = process_events(response.json())
			ApiService.events = [Event(**api_event) for api_event in api_events]
		return ApiService.events


	def format_body(self):
		base_dict = {
			"event_search": {
				"sort": "default",
				"page_size": 100,
			}
		}
		return base_dict
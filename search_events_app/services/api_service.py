from search_events_app.models.event import Event
from search_events_app.services.dummy_api import DummyApi


def get_events():

	api_events = DummyApi().get()
	return [Event(**api_event) for api_event in api_events]

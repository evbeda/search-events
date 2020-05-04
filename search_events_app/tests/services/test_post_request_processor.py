from django.test import TestCase

from search_events_app.models.event import Event
from search_events_app.views import DTOFilter

from search_events_app.services.post_request_processor import validate_filters

class TestPostRequestProcessor(TestCase):
    def setUp(self):
        self.dto_filter = DTOFilter()
        self.dto_filter.country = "Argentina"

    def test_validate_filters_true(self):
        event = Event("Event1", "https://google.com", country="Argentina")
        result = validate_filters(event, self.dto_filter)

        self.assertTrue(result)

    def test_validate_filters_false(self):
        event = Event("Event1", "https://google.com", country="Brazil")
        
        result = validate_filters(event, self.dto_filter)

        self.assertFalse(result)

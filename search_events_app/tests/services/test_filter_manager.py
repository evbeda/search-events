from unittest.mock import MagicMock

from django.test import TestCase

from search_events_app.models.event import Event
from search_events_app.services.filter_manager import FilterManager


class TestFilterManager(TestCase):
    def setUp(self):
        self.event1 = Event('Event1', 'wwww.google.com', 'Argentina')
        self.event2 = Event('Event2', 'wwww.google.com', 'United States')
        self.event3 = Event('Event3', 'wwww.google.com', 'Ireland')
        self.event4 = Event('Event4', 'wwww.google.com', 'Argentina')
        self.event5 = Event('Event5', 'wwww.google.com', 'Chile')
        self.events = [
            self.event1,
            self.event2,
            self.event3,
            self.event4,
            self.event5
        ]

    def test_filter_events(self):
        expected = {'country': 'ar'}
        mock_request = MagicMock()
        mock_request.GET = MagicMock()
        mock_request.GET.get = MagicMock(return_value='AR')

        FilterManager.apply_filter(mock_request)

        self.assertEqual(FilterManager.latest_filter, expected)

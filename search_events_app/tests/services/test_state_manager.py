from django.test import TestCase

from search_events_app.models.event import Event
from search_events_app.services.state_manager import StateManager


class TestStateManager(TestCase):
    def setUp(self):
        self.events = [
            Event('Event1', 'wwww.google.com', 'Argentina'),
            Event('Event2', 'wwww.google.com', 'United States'),
            Event('Event3', 'wwww.google.com', 'Ireland'),
            Event('Event4', 'wwww.google.com', 'Argentina'),
            Event('Event5', 'wwww.google.com', 'Chile'),
        ]

    def test_set_events(self):
        StateManager.set_events(self.events)
        result = StateManager.events
        self.assertEqual(result, self.events)

    def test_reset_events(self):
        StateManager.reset_events()
        result = StateManager.events
        self.assertIsNone(result)

    def test_get_last_searched_events(self):
        StateManager.events = self.events
        result = StateManager.get_last_searched_events()
        self.assertEqual(result, self.events)

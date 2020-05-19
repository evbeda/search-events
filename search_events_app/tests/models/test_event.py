from django.test import TestCase

from search_events_app.models.country import Country
from search_events_app.models.event import Event
from search_events_app.models.feature import Feature


class TestEvent(TestCase):

    def setUp(self):
        self.feature = Feature('Website Widgets')

    def test_event_without_country(self):
        event = Event('Name', 'www.google.com')
        self.assertEqual(event.country, None)

    def test_event_basic_info(self):
        country = Country.objects.create(label='Argentina', code='AR', eventbrite_id='1234')
        event = Event(
            'Evento1', 'www.google' +
            '.com', country, self.feature
        )
        self.assertEqual(event.name, 'Evento1')
        self.assertEqual(event.country, country)
        self.assertEqual(event.feature, self.feature)
        self.assertEqual(event.url, 'www.google.com')

    def test_event_with_two_features(self):
        feature = Feature('Reserved Seating')        
        event = Event(
            'Futbol',
            'www.google.com',
            feature=[self.feature, feature]
        )
        self.assertEqual(len(event.feature), 2)

    def test_events_more_items(self):
        dict_event = {
            'name': 'Carats world tour',
            'organizer_name': 'Seung',
            'country': 'Italy',
            'url': (
                'https://www.eventbrite.com/e/carats-world-tour-tickets'
                '-102537931714?aff=ebdssbonlinesearch'
                ),
            'start_date': '2020-07-20',
            'features': ['EB Studio', 'Facebook'],
            'language': 'English',
            'category': 'Music',
            'format_': 'Festival'
        }
        event = Event(**dict_event)
        self.assertEqual(event.language, 'English')
        self.assertEqual(event.category, 'Music')
        self.assertEqual(event.format, 'Festival')

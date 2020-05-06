
import django
import requests
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_events.settings.dev')
django.setup()

from search_events_app.models.country import Country

Country.objects.all().delete()
response = requests.get('https://www.evbqaapi.com/v3/system/countries/?token=QF44722VLJLXURKY43HZ')
countries_list = response.json().get('countries')
for country in countries_list:
	country['eventbrite_id'] = '0'
	country = Country(**country)
	response_place = requests.get(f'https://www.evbqaapi.com/v3/destination/search/places/?q={country.name}&token=QF44722VLJLXURKY43HZ')
	places = response_place.json().get('places')
	if places:
		for place in places:
			if place.get('place_type') == 'country':
				country.eventbrite_id = place.get('id')
	country.save()

import os
import django
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_events.settings.dev')
django.setup()

from search_events_app.models.country import Country

response = requests.get("https://restcountries.eu/rest/v2/all")
countries_list = response.json()
for country in countries_list:
	Country(**country).save()

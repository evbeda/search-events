import csv
import os

from django.db import migrations


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'data_cities.csv')


def get_cities():
    with open(my_file, newline='\n') as csvfile:
        cities = list(csv.reader(csvfile, delimiter=','))
        return cities


def save_cities(apps, schema_editor):
    City = apps.get_model('search_events_app', 'City')
    
    cities = get_cities()
    for city in cities:
        City.objects.create(code='', name=city[0], country=city[1])


class Migration(migrations.Migration):

    dependencies = [
        ('search_events_app', '0013_populate_usa_cities'),
    ]

    operations = [
        migrations.RunPython(save_cities),
    ]

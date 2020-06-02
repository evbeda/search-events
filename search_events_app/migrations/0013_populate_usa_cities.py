import csv
import os

from django.db import migrations


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'data_usa_cities.csv')


def get_cities():
    with open(my_file, newline='\n') as csvfile:
        cities = list(csv.reader(csvfile, delimiter=','))
        return cities


def save_cities(apps, schema_editor):
    City = apps.get_model('search_events_app', 'City')
    
    cities = get_cities()
    for city in cities:
        City.objects.create(code=city[0], name=city[2], country='US')


class Migration(migrations.Migration):

    dependencies = [
        ('search_events_app', '0012_city'),
    ]

    operations = [
        migrations.RunPython(save_cities),
    ]

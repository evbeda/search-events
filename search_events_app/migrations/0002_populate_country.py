import csv
import os

from django.db import migrations


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'data_country.csv')


def get_countries():
    with open(my_file, newline='\n') as csvfile:
        countries = list(csv.reader(csvfile, delimiter=','))
        return countries


class Migration(migrations.Migration):
    dependencies = [
        ('search_events_app', '0001_initial'),
    ]
    countries = get_countries()
    operations = [
        migrations.RunSQL(
            ''.join([
                f"INSERT INTO search_events_app_country (name, alpha_2_code, eventbrite_id) VALUES ( '{c[1]}', '{c[2]}', '{c[3]}');"
                for c in countries
            ])
        )
    ]

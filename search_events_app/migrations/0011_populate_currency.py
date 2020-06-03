from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('search_events_app', '0010_currency'),
    ]

    operations = [
        migrations.RunSQL(
            '''
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('United States Dollar','USD');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Euro','EUR');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Argentine Peso','ARS');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Australian Dollar','AUD');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Brazilian Real','BRL');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Canadian Dollar','CAD');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Chilean Peso','CLP');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Hong Kong Dollar','HKD');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Mexican Peso','MXN');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('New Zealand Dollar','NZD');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Pound Sterling','GBP');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Singapore Dollar','SGD');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Swiss Franc','CHF');
                INSERT INTO main.search_events_app_currency (name, code) VALUES ('Rest of the Word','ROW');
            '''
        )
    ]

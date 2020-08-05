from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('search_events_app', '0014_populate_row_cities'),
    ]

    operations = [
        migrations.RunSQL(
            '''
                INSERT INTO main.search_events_app_feature (name, code) VALUES ('Facebook', 'FB');
            '''
        )
    ]

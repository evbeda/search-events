from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('search_events_app', '0002_populate_country'),
    ]
    
    operations = [
        migrations.RunSQL(
            '''
                INSERT INTO search_events_app_language (name, code) VALUES ('Arabic', 'ar');
                INSERT INTO search_events_app_language (name, code) VALUES ('Danish', 'da');
                INSERT INTO search_events_app_language (name, code) VALUES ('German', 'de');
                INSERT INTO search_events_app_language (name, code) VALUES ('English', 'en');
                INSERT INTO search_events_app_language (name, code) VALUES ('Spanish', 'es');
                INSERT INTO search_events_app_language (name, code) VALUES ('French', 'fr');
                INSERT INTO search_events_app_language (name, code) VALUES ('Italian', 'it');
                INSERT INTO search_events_app_language (name, code) VALUES ('Japanese', 'ja');
                INSERT INTO search_events_app_language (name, code) VALUES ('Korean', 'ko');
                INSERT INTO search_events_app_language (name, code) VALUES ('Dutch', 'nl');
                INSERT INTO search_events_app_language (name, code) VALUES ('Polish', 'pl');
                INSERT INTO search_events_app_language (name, code) VALUES ('Portuguese', 'pt');
                INSERT INTO search_events_app_language (name, code) VALUES ('Russian', 'ru');
                INSERT INTO search_events_app_language (name, code) VALUES ('Swedish', 'sv');
                INSERT INTO search_events_app_language (name, code) VALUES ('Chinese', 'zh');
            '''
        )
    ]

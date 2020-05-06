from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_events_app', '0004_language'),
    ]

    operations = [
        migrations.RunSQL(
            """INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('1', 'Arabic', 'ar');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('2', 'Danish', 'da');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('3', 'German', 'de');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('4', 'English', 'en');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('5', 'Spanish', 'es');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('6', 'French', 'fr');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('7', 'Italian', 'it');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('8', 'Japanese', 'ja');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('9', 'Korean', 'ko');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('10', 'Dutch', 'nl');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('11', 'Polish', 'pl');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('12', 'Portuguese', 'pt');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('13', 'Russian', 'ru');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('14', 'Swedish', 'sv');
            INSERT INTO 'main'.'search_events_app_language' ('id', 'name', 'code') VALUES ('15', 'Chinese', 'zh');"""
        )
    ]

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_events_app', '0004_language'),
    ]

    operations = [
        migrations.RunSQL(
            """
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('1', 'Arabic', 'ar');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('2', 'Danish', 'da');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('3', 'German', 'de');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('4', 'English', 'en');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('5', 'Spanish', 'es');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('6', 'French', 'fr');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('7', 'Italian', 'it');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('8', 'Japanese', 'ja');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('9', 'Korean', 'ko');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('10', 'Dutch', 'nl');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('11', 'Polish', 'pl');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('12', 'Portuguese', 'pt');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('13', 'Russian', 'ru');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('14', 'Swedish', 'sv');
                INSERT INTO 'search_events_app_language' ('id', 'name', 'code') VALUES ('15', 'Chinese', 'zh');
            """
        )
    ]

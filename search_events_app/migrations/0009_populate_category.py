from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
		('search_events_app', '0008_category'),
	]

	operations = [
		migrations.RunSQL(
			'''
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Auto, Boat & Air', 'ABA');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Business & Professional', 'BP');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Charity & Causes', 'CHC');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Community & Culture', 'CC');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Family & Education', 'FE');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Fashion & Beauty', 'FB');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Film, Media & Entertainment', 'FME');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Food & Drink', 'FD');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Government & Politics', 'GP');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Health & Wellness', 'HW');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Hobbies & Special Interest', 'HSI');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Home & Lifestyle', 'HL');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Music', 'M');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Other', 'O');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Performing & Visual Arts', 'PVA');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Religion & Spirituality', 'RS');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('School Activities', 'SA');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Science & Technology', 'ST');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Seasonal & Holiday', 'SH');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Travel & Outdoor', 'TO');
				INSERT INTO main.search_events_app_category (name, code) VALUES ('Unknown', 'U');
			'''
		)
	]

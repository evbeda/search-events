from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
		('search_events_app', '0004_feature'),
	]

	operations = [
		migrations.RunSQL(
			'''
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Add Ons', 'AO');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Custom Question', 'CQ');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Donation', 'DO');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('EB Studio', 'ES');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Group Registration', 'GR');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Repeating Event', 'RE');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Reserved Seating', 'RS');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Wait List', 'WL');
				INSERT INTO main.search_events_app_feature (name, code) VALUES ('Website Widgets', 'WW');
			'''
		)
	]

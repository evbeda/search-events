from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
		('search_events_app', '0004_feature'),
	]

	operations = [
		migrations.RunSQL(
			'''
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('1', 'Add Ons', 'AO');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('2', 'Bulk Attendee Upload', 'BA');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('3', 'Custom Question', 'CQ');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('4', 'EB Studio', 'ES');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('5', 'Repeating Event', 'RE');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('6', 'Reserved Seating', 'RS');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('7', 'Website Widgets', 'WW');
			'''
		)
	]

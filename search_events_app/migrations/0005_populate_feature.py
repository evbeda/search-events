from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
		('search_events_app', '0004_feature'),
	]

	operations = [
		migrations.RunSQL(
			'''
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('1', 'Embedded Checkout', 'EC');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('2', 'Reserved Seating', 'RS');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('3', 'Repeating Event', 'RE');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('4', 'Custom Question', 'CQ');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('5', 'Add Ons', 'AO');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('6', 'EB Studio', 'ES');
				INSERT INTO main.search_events_app_feature (id, name, code) VALUES ('7', 'Bulk Attendee Upload', 'BAU');
			'''
		)
	]
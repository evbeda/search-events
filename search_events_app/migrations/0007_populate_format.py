from django.db import migrations


class Migration(migrations.Migration):
	dependencies = [
		('search_events_app', '0006_format'),
	]

	operations = [
		migrations.RunSQL(
			'''
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('AS', 'Appearance or Signing');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('A', 'Attraction');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('CTR', 'Camp, Trip, or Retreat');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('CTW', 'Class, Training, or Workshop');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('CP', 'Concert or Performance');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('Ce', 'Conference');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('Cn', 'Convention');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('DG', 'Dinner or Gala');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('FF', 'Festival or Fair');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('GC', 'Game or Competition');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('MNE', 'Meeting or Networking Event');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('O', 'Other');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('PSG', 'Party or Social Gathering');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('REE', 'Race or Endurance Event');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('R', 'Rally');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('S', 'Screening');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('ST', 'Seminar or Talk');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('Tr', 'Tour');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('Tt', 'Tournament');
			    INSERT INTO main.search_events_app_format (code, name) VALUES ('TCWE', 'Tradeshow, Consumer Show, or Expo');
			'''
		)
	]

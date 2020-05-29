from django.test import TestCase

from search_events_app.services.db.db_response_processor import (
	process_events,
	get_country,
	get_language,
	get_organizer,
	get_url,
)


class TestDBResponseProcessor(TestCase):
	def test_process_events(self):
		mock_db_response = [
			(
				99894936444,
				'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
				'Business & Professional',
				'Meeting or Networking Event',
				None,
				'Adam Kurtz Org',
				'US',
				'2020-12-16',
				'en_US'
			),
			(
				104429836452,
				'Shawn Mendes The Virtual Tour',
				'Music',
				'Concert or Performance',
				'Mia Discenza',
				'Mia Discenza Org',
				None,
				'2020-05-16',
				'en_US'
			)
		]
		result = process_events(mock_db_response)
		expected_result = {
			'name': 'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
			'url': 'https://www.eventbrite.com/e/99894936444',
			'language': 'English',
			'start_date': '2020-12-16',
			'category': 'Business & Professional',
			'format_': 'Meeting or Networking Event',
			'organizer': 'Adam Kurtz Org',
			'country': 'United States',
			'admin_url': 'https://www.eventbrite.com/myevent?eid=99894936444',
		}

		self.assertIsInstance(result[0], dict)
		self.assertEqual(len(result), 2)
		self.assertEqual(result[0], expected_result)

	def test_get_country(self):
		item = (
				99894936444,
				'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
				'Business & Professional',
				'Meeting or Networking Event',
				'Adam Kurtz',
				'Adam Kurtz Org',
				'US',
				'2020-12-16',
				'en_US'
		)
		country = get_country(item)

		self.assertEqual(country, 'United States')

	def test_get_none_country(self):
		item = (
			99894936444,
			'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
			'Business & Professional',
			'Meeting or Networking Event',
			'Adam Kurtz'
			'Adam Kurtz Org',
			'ZX',
			'2020-12-16',
			'en_US'
		)

		country = get_country(item)

		self.assertIsNone(country)

	def test_get_language(self):
		item = (
			99894936444,
			'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
			'Business & Professional',
			'Meeting or Networking Event',
			'Adam Kurtz',
			'Adam Kurtz Org',
			'ZX',
			'2020-12-16',
			'en_US'
		)

		result = get_language(item)

		self.assertEqual(result, "English")

	def test_url(self):
		item = (
			99894936444,
			'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
			'Business & Professional',
			'Meeting or Networking Event',
			'Adam Kurtz',
			'ZX',
			'2020-12-16',
			'en_US'
		)

		result = get_url(item)

		self.assertEqual(result, 'https://www.eventbrite.com/e/99894936444')

	def test_get_organizer_name_without_organizer(self):
		item = (
			99894936444,
			'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
			'Business & Professional',
			'Meeting or Networking Event',
			None,
			'Adam Kurtz Organization',
			'ZX',
			'2020-12-16',
			'en_US'
		)

		result = get_organizer(item)

		self.assertEqual(result, 'Adam Kurtz Organization')

	def test_none_organizer(self):
		item = (
			99894936444,
			'LEARN WHAT IT TAKES TO BUY A HOME IN LAS VEGAS (FREE WINE &amp; PIZZA)',
			'Business & Professional',
			'Meeting or Networking Event',
			' ',
			' ',
			'ZX',
			'2020-12-16',
			'en_US'
		)

		result = get_organizer(item)

		self.assertIsNone(result)

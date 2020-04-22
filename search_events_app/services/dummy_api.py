
class DummyApi:

	events = [
		{
			'name':'Lollapaloza',
			'organizer_name': 'Productora 1',
			'country': 'Argentina',
			'url':'https://www.eventbrite.com/e/summerton-virtual-whisky-festival-tickets-101800967434?aff=ebdssbonlinesearch',
			'start_date': '2020-05-02',
			'features':['Embedded Checkout', 'Custom Question'],
			'language': 'Spanish',
			'category': 'Music',
			'format': 'Festival'
		},
		{
			'name': 'Football match',
			'organizer_name': 'UEFA',
			'country': 'Spain',
			'url':'https://www.eventbrite.com/e/2020-mwhsports-football-college-camp-tours-tickets-96353506933?aff=ebdssbonlinesearch',
			'start_date':'2018-03-18',
			'features': ['Add-ons'],
			'language': 'English',
			'category': 'Sports and Fitness',
			'format': 'Game'
		},
		{
			'name': 'Curso manejo de cesped',
			'organizer_name': 'ACP',
			'country': 'Argentina',
			'url':'https://www.eventbrite.com.ar/e/curso-de-cuidado-y-manejo-de-cesped-en-predios-deportivos-registration-84144934765?aff=ebdssbonlinesearch',
			'start_date': '2019-08-03',
			'features': [],
			'language': 'Spanish',
			'category': 'Business',
			'format': 'Class'
		},
		{
			'name': 'Trainning',
			'organizer_name': 'Productor A',
			'country': 'England',
			'url': 'https://www.eventbrite.com.ar/e/entrenamiento-actitudinal-para-equipos-y-deportistas-tickets-102970383188?aff=ebdssbonlinesearch',
			'start_date': '2020-09-17',
			'features': ['EB Studio'],
			'language': 'English',
			'category': 'Health',
			'format': 'Class',
		},
		{
			'name': 'Live Webinar: Minnesota State University',
			'organizer_name': 'Minnesota State University',
			'country': 'United States',
			'url': 'https://www.eventbrite.com/e/live-webinar-minnesota-state-university-tickets-102275081522?aff=ebdssbonlinesearch',
			'start_date': '2021',
			'features': ['Add-ons', 'Embedded Checkout'],
			'language': 'English',
			'category': 'School Activities',
			'format': 'Conference',
		},
		{
			'name': 'Cinco de mayo',
			'organizer_name': 'Pompano Houseives',
			'country': 'Argentina',
			'url':'https://www.eventbrite.com/e/cinco-de-mayo-tickets-85998809755?aff=ebdssbonlinesearch',
			'start_date': '2020-04-09',
			'features': [],
			'language': 'Spanish',
			'category': 'Holidays',
			'format': 'Party'
		},
		{
			'name':'Virtual gathering',
			'organizer_name': 'Pollen',
			'country': 'Ireland',
			'url': 'https://www.eventbrite.com/e/are-you-ok-a-virtual-gathering-tickets-100056485642?aff=ebdssbonlinesearch',
			'start_date': '2018-11-08',
			'features': ['Bulk attendee upload'],
			'language': 'English',
			'category': 'Community',
			'format': 'Convention'
		},
		{
			'name': 'Carats world tour',
			'organizer_name': 'Seung',
			'country': 'Italy',
			'url': 'https://www.eventbrite.com/e/carats-world-tour-tickets-102537931714?aff=ebdssbonlinesearch',
			'start_date': '2020-07-20',
			'features': ['EB Studio'],
			'language': 'English',
			'category': 'Music',
			'format': 'Festival'
		},
		{
			'name': 'Virtual stitch & bitch',
			'organizer_name': 'Fashion Revolution',
			'country': '',
			'url':'https://www.eventbrite.co.uk/e/fashion-question-time-tickets-90925824589?aff=ebdssbonlinesearch',
			'start_date': '2021-01-30',
			'features': ['Repeating event'],
			'language': 'English',
			'category': 'Fashion',
			'format': 'Expo',
		},
	]

	def get(self):
		return self.events

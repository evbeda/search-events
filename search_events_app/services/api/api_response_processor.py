from search_events_app.models import Country


def process_events(response):
    data = response.get('events')
    events = []
    if data:
        data = data.get('results')
        for item in data:
            event_dict = {
                'name': item.get('name'),
                'url': get_url(item),
                'language': get_language(item),
                'start_date': item.get('start_date'),
                'category': get_tag(item, 'EventbriteCategory'),
                'format_': get_tag(item, 'EventbriteFormat'),
                'organizer': item.get('primary_organizer').get('name'),
                'country': get_country(item),

            }
            events.append(event_dict)
    return events


def get_tag(item, criteria):
    tags = item.get('tags')
    for tag in tags:
        if tag['prefix'] == criteria:
            return tag['display_name']


def get_country(item):
    venue = item.get('primary_venue')
    if venue:
        address = venue.get('address')
        if address:
            alpha2code = address.get('country')
            if alpha2code:
                country = Country.objects.get(alpha_2_code=alpha2code)
                return country.name


def get_language(item):
    lang = item.get('language')
    return lang.split('-')[0]


def get_url(item):
    return item.get('url').replace('evbqa', 'eventbrite')

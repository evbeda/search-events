from search_events_app.models.country import Country


def process_events(data):
    events = []
    if data:
        for item in data:
            event_dict = {
                'url': get_url(item),
                'name': item[1],
                'category': item[2],
                'format_': item[3],
                'organizer': item[4],
                'country': get_country(item),
                'start_date': item[6],
                'language': get_language(item),

            }
            events.append(event_dict)
    return events


def get_country(item):
    try:
        country = Country.objects.get(alpha_2_code=item[5])
        return country.name
    except Exception:
        return None


def get_language(item):
    lang = item[7]
    return lang.split('_')[0]


def get_url(item):
    return f'https://www.eventbrite.com/e/{item[0]}'

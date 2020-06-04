from search_events_app.models import (
    Country,
    Language,
)


def process_events(data):
    events = []
    if data:
        for item in data:
            event_dict = {
                'url': get_url(item),
                'name': item[1],
                'category': item[2],
                'format_': item[3],
                'organizer': get_organizer(item),
                'country': get_country(item),
                'start_date': item[7],
                'language': get_language(item),
                'admin_url': get_admin_url(item),
                'eb_studio_url': get_eb_studio_url(item),
            }
            events.append(event_dict)
    return events


def get_country(item):
    try:
        country = Country.objects.get(alpha_2_code=item[6])
        return country.name
    except Exception:
        return None


def get_language(item):
    lang = item[8].split('_')[0]
    language = Language.objects.get(code=lang)
    return language.name


def get_url(item):
    return f'https://www.eventbrite.com/e/{item[0]}'


def get_organizer(item):
    if item[4] and item[4].strip():
        return item[4]
    if item[5] and item[5].strip():
        return item[5]
    return None


def get_eb_studio_url(item):
    if item[9]:
        return f'https://{item[9]}'
    return None


def get_admin_url(item):
    return f'https://www.eventbrite.com/myevent?eid={item[0]}'

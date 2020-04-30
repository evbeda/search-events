from search_events_app.models.country import Country


def process_events(response):
    data = response["events"]["results"]

    events = []
    for item in data:
        event_dict = {
            "name": item.get("name"),
            "url": item.get("url"),
            "language": item.get("language"),
            "start_date": item.get("start_date"),
            "category": get_tag(item, "EventbriteCategory"),
            "format_": get_tag(item, "EventbriteFormat"),
            "organizer": item.get("primary_organizer").get("name"),
            "country": get_country(item),

        }
        events.append(event_dict)
    return events


def get_tag(item, criteria):
    tags = item.get("tags")
    for tag in tags:
        if tag["prefix"] == criteria:
            return tag["display_name"]


def get_country(item):
    venue = item.get("primary_venue")
    if venue:
        address = venue.get("address")
        if address:
            alpha2code = address.get("country")
            if alpha2code:
                country = Country.objects.get(alpha_2_code=alpha2code)
                return country.name

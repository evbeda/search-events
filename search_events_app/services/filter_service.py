def filter_events(request, list_events):
    list_events = apply_country_filter(request, list_events)
    return list_events


def apply_country_filter(request, list_events):
    qs_country = request.GET.get('country')
    if (qs_country):
        list_events = [
            event for event in list_events if event.country
            in qs_country and event.country != ''
        ]
    return list_events

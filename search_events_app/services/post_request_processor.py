def post_process_events(events, dto_filter):
    events_response = [event for event in events if validate_filters(event, dto_filter)]
    return events_response


def validate_filters(event, dto_filter):
    return all([
            validate_country(event, dto_filter),
        ])


def validate_country(event, dto_filter):
    if not dto_filter.country:
        return True
    return event.country == dto_filter.country

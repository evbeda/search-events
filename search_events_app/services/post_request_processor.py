def post_process_events(events, dto_filter):
    events_response = [event for event in events if validate_filters(event, dto_filter)]
    return events_response


def validate_filters(event, dto_filter):
    return all([
            event.country == dto_filter.country
        ])
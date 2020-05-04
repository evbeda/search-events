def post_process_events(events, DTOfilters):
    events_response = [event for event in events if event.country == DTOfilters.country]
    return events_response

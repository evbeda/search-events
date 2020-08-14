from search_events_app.utils import SpecificEventsQueryParameters
from search_events_app.utils import FindFeatureQueryParameters


class QueryParameterFactory:

    @classmethod
    def get_query_parameters(cls, request):
        if 'SpecificEvent' in request.path:
            return SpecificEventsQueryParameters
        elif 'FindFeature' in request.path:
            return FindFeatureQueryParameters

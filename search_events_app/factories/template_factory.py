class TemplateFactory:

    @classmethod
    def get_template(cls, request):
        if 'SpecificEvent' in request.path:
            return 'specific_event.html'
        elif 'FindFeature' in request.path:
            return 'find_feature.html'

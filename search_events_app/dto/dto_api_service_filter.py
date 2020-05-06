class DTOApiServiceFilter:
    
    def __init__(self, **kwargs):
        self.type = kwargs.get('type')
        self.value = kwargs.get('value')

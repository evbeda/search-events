class DTODBServiceFilter:

    def __init__(self, **kwargs):
        self.join_value = kwargs.get('join_query', '')
        self.where_value = kwargs.get('where_query', '')

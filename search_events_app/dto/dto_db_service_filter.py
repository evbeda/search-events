class DTODBServiceFilter:

    def __init__(self, **kwargs):
        self.join_query = kwargs.get('join_query', '')
        self.where_query = kwargs.get('where_query', '')

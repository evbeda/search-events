class DTODBServiceFilter:

    def __init__(self, **kwargs):
        self.select_query = kwargs.get('select_query', '')
        self.where_query = kwargs.get('where_query', '')
        self.join_query = kwargs.get('join_query', '')
        self.group_query = kwargs.get('group_query', '')

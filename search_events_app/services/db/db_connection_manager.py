from pyhive import presto


class ConnectionManager:
    connection = None
    url = 'presto-tableau.prod.dataf.eb'

    @classmethod
    def connect(cls, user_okta, password_okta):
        if cls.connection:
            cls.connection.close()
        connection = presto.connect(
            cls.url,
            8443,
            user_okta,
            password=password_okta,
            protocol='https',
        )
        cls.connection = connection
        return cls.connection.cursor()

    @classmethod
    def get_connection(cls):
        if cls.connection:
            return cls.connection.cursor()

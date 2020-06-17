from pyhive import presto


class ConnectionManager:
    connections = {}
    username = None
    url = 'presto-tableau.prod.dataf.eb'

    @classmethod
    def connect(cls, user_okta, password_okta, session):
        connection = presto.connect(
            cls.url,
            8443,
            user_okta,
            password=password_okta,
            protocol='https',
        )

        cls.connections[session.session_key] = connection
        return connection.cursor()

    @classmethod
    def get_connection(cls, session):
        if cls.connections.get(session.session_key):
            return cls.connections[session.session_key].cursor()

    @classmethod
    def disconnect(cls, session):
        cls.connections[session.session_key].close()
        del cls.connections[session.session_key]

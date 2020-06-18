from pyhive import presto
import datetime


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
        cls.check_and_clean_connections()
        cls.connections[session.session_key] = {}
        cls.connections[session.session_key]['connection'] = connection
        cls.connections[session.session_key]['date'] = datetime.date.today()
        return connection.cursor()

    @classmethod
    def get_connection(cls, session_key):
        if cls.connections.get(session_key):
            return cls.connections[session_key]['connection'].cursor()

    @classmethod
    def disconnect(cls, session):
        cls.connections[session.session_key]['connection'].close()
        del cls.connections[session.session_key]

    @classmethod
    def check_and_clean_connections(cls):
        expires = datetime.date.today()-datetime.timedelta(days=1)
        sessions_to_delete = []
        if len(cls.connections.keys()) > 50:
            for session_key, connection_dict in cls.connections.items():
                if connection_dict['date'] < expires:
                    sessions_to_delete.append(session_key)
            for session_key in sessions_to_delete:
                del cls.connections[session_key]


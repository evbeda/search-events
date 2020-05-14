from pyhive import presto
from django.conf import settings

from search_events_app.exceptions.presto_error import PrestoError


class ConnectionManager:
    connection = None

    @classmethod
    def connect(cls):
        if not cls.connection:
            connection = presto.connect(
                'presto-tableau.prod.dataf.eb',
                8443,
                settings.USER_OKTA,
                password=settings.PASSWORD_OKTA,
                protocol='https',
            )
            cls.connection = connection
        return cls.connection.cursor()

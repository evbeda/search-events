from pyhive import presto
from django.conf import settings


class ConnectionManager:
    connection = None

    @classmethod
    def connect(cls):
        if not cls.connection:
            try:
                connection = presto.connect(
                    'presto-tableau.prod.dataf.eb',
                    8443,
                    settings.USER_OKTA,
                    password=settings.PASSWORD_OKTA,
                    protocol='https',
                )
                cls.connection = connection
            except Exception as e:
                message = e.args[0]['message']
                raise PrestoError(message)
        return cls.connection.cursor()


class PrestoError(Exception):
    def __init__(self, error_message):
        self.args = (self.get_message(error_message),)

    def get_message(self, error_message):
        if 'NewConnectionError' in error_message:
            # Raised when not connected to the VPN
            message = error_message.split('>:')[1].split("'))")[0].strip()
            message += '.<br>Make sure you are connected to the VPN.'
        elif 'SSLCertVerificationError' in error_message:
            # Raised when certificate not in env var
            message = error_message.split("(1, '")[1].split("')))")[0].strip()
            message += '.<br>Update your certificate '
            message += '(<a href="https://docs.evbhome.com/intro/self_signed_certs.html">link</a>).'
        elif 'Could not find a suitable TLS CA certificate' in error_message:
            # Raised when certificate file not found
            message = error_message
            message += '.<br>Download the certificate '
            message += '(<a href="https://docs.evbhome.com/intro/self_signed_certs.html">link</a>) '
            message += 'and save in the previous path.'
        elif ('Invalid credentials' in error_message) or ('Malformed decoded credentials' in error_message):
            # Raised when wrong or empty okta username/password
            message = error_message.split('<pre>')[1].split('</pre>')[0].strip()
            message += '.<br>Check your okta username and password.'
        else:
            message = error_message
        return message

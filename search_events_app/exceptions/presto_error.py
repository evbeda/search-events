from requests.exceptions import (
    SSLError,
    ConnectionError,
)


class PrestoError(Exception):
    def __init__(self, error_message):
        if isinstance(error_message, ConnectionError):
            self.message = 'Make sure you are connected to the VPN!'
        elif isinstance(error_message, SSLError):
            # Raised when certificate not in env var
            self.message = 'Update your certificate from this <a href="https://docs.evbhome.com/intro/self_signed_certs.html">link</a>.'
        elif isinstance(error_message, OSError):
            # Raised when certificate file not found
            self.message = 'Download the certificate '
            self.message += '<a href="https://docs.evbhome.com/intro/self_signed_certs.html">link</a> '
            self.message += 'and update the path of your environment variable.'
        else:
            self.message = error_message

class OktaCredentialError(Exception):
    def __init__(self):
        self.message = 'Invalid Okta user or password'

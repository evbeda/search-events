
from .base import *
import dj_database_url


ALLOWED_HOSTS = [
    '*',
]


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'PORT': '',
    }
}

DB_FROM_ENV = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(DB_FROM_ENV)

# Application definition

MIDDLEWARE += [  # noqa
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_prod')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

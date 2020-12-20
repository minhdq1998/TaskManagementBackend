
import configparser

from .base import *

# Get the configuration files
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('base','secret')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('postgres','db'),
        'USER': config.get('postgres','user'),
        'PASSWORD': config.get('postgres','password'),
        'HOST': config.get('postgres','host'),
        'PORT': config.get('postgres','port')
    }
}

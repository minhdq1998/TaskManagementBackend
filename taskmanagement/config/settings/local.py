
from .base import *
import configparser

# Get the configuration files
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('base','secret')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

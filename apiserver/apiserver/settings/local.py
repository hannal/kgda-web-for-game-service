from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webdb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'db',  # docker
        'PORT': '5432',  # docker
    },
}

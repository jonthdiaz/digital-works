from dw.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


DATABASES = {
    'default':
        {'USER': 'dw_admin',
         'HOST': '127.0.0.1',
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'dw_db',
         'PORT': '',
         'PASSWORD': 'dw_admin'}
}

if not DEBUG:
    DATABASES['default'] = dj_database_url.config()

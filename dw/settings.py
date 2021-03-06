import os
import dj_database_url
from django.conf import settings


ADMINS = (
    ('Jonathan Diaz', 'jon.erikfer@hotmail.com'),
)

MANAGERS = ADMINS

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for dw project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# filter errors allowed host
def skip_suspicious_operations(record):
    if record.name == 'django.security.DisallowedHost':
        return False
    return True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e=x#inqm8w^qam%g(^1i)tu3@%^l-h6znf#srpfp8)(3iyh*q-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

ALLOWED_HOSTS = ['digital-workers.co', '0.0.0.0', '127.0.0.1',
                 'www.digital-workers.co', '45.55.214.123']


# Application definition
ROOT_URLCONF = 'dw.urls'

WSGI_APPLICATION = 'dw.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])
# STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'dw', 'static'),
    os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content']),
)
SITE_ID = 1
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    # 'johnny.middleware.LocalStoreClearMiddleware',
    # 'johnny.middleware.QueryCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.gzip.GZipMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'cms.context_processors.cms_settings',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'dw.context_processors.send_debug_to_template',
    'constance.context_processors.config',
)

TEMPLATE_DIRS = (
    os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['templates']),
)

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'django_extensions',
    'treebeard',
    'constance',
    'gtm',
    'kopy',
    'dw',
    'djrill',
    'profiles',
    'applications',
    'utils',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'skip_suspicious_operations': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_suspicious_operations,
        }

    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(name)s %(asctime)s %(module)s %(process)d %(thread)d %(pathname)s@%(lineno)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(name)s %(filename)s@%(lineno)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'skip_suspicious_operations'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console', ],
            'level': 'INFO',
        }
    }
}

LANGUAGES = (
    ## Customize this
    ('es', gettext('es')),
    # ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'es',
            'public': True,
            'redirect_on_fallback': True,
            'name': gettext('es'),
            'hide_untranslated': False,
        },
        {
            'code': 'en',
            'public': True,
            'redirect_on_fallback': True,
            'name': gettext('en'),
            'hide_untranslated': False,
        },
    ],
    'default': {
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    # Customize this
    ('shared/layout.html', 'layout'),
    ('base.html', 'base'),
    ('shared/dw/layout.html', 'layout_dw'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {'USER': 'dw_admin',
         'HOST': 'localhost',
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'dw_db',
         'PORT': '5432',
         'PASSWORD': 'dw_admin'}
}

# print('debug: %s' % settings.DEBUG)

# if not DEBUG:
#     DATABASES['default'] = dj_database_url.config()


MIGRATION_MODULES = {
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django'
}

DEFAULT_FROM_EMAIL = 'jonthdiaz@gmail.com'
SERVER_EMAIL = 'jonthdiaz@gmail.com'


EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = 'PaWrBqGZlMLb4dh8IIgUfQ'


# some johnny settings
CACHES = {
    'default': dict(
        BACKEND='johnny.backends.memcached.MemcachedCache',
        LOCATION=['127.0.0.1:11211'],
        JOHNNY_CACHE=True,
    )
}
JOHNNY_MIDDLEWARE_KEY_PREFIX = 'jc_digitalworkers'

# CMS_CONTENT_CACHE_DURATION = 0

# google tag manager
GOOGLE_TAG_ID = 'GTM-WDTLL5'

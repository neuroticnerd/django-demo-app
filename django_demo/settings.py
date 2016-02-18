""" settings for django_demo project: intended for Django 1.8.9 """
import os

from ast import literal_eval
from os.path import abspath, dirname, join


# retrieve python objects from strings in environment variables
def hydrate(data):
    if isinstance(data, basestring):
        return literal_eval(data)
    return data


# super simple function for grabbing environment vars
def env(key, default=None, coax=str):
    value = os.environ.get('DJANGO_DEMO_' + key, default)
    if value is None:
        return value
    return coax(value)


SITE_ID = env('SITE_ID', 1, int)
BASE_DIR = dirname(dirname(abspath(__file__)))

DEBUG = env('DEBUG', True, bool)

# default key should never be used in production
DEFAULT_SECRET_KEY = 'j1^szqq)h*bmvv2p8!j(uzcdn)9f*yvp5vwh_w8@g5_(u@uns)'
SECRET_KEY = env('SECRET_KEY', DEFAULT_SECRET_KEY)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', ['*'], hydrate)
WSGI_APPLICATION = 'django_demo.wsgi.application'
ROOT_URLCONF = 'django_demo.urls'

STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', join(BASE_DIR, 'static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = env('MEDIA_ROOT', join(BASE_DIR, 'media'))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'bootstrap3',

    'django_demo.main',
    'django_demo.actions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
)

DJANGO_TEMPLATE_OPTIONS = {
    'context_processors': [
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.debug',
        'django.template.context_processors.i18n',
        'django.template.context_processors.media',
        'django.template.context_processors.static',
        'django.template.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django_demo.context_processors.current_site',
    ],
    'debug': env('TEMPLATE_DEBUG', DEBUG, bool),
}
DJANGO_TEMPLATES = {
    'NAME': 'django',
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        join(BASE_DIR, 'django_demo/templates'),
    ],
    'OPTIONS': DJANGO_TEMPLATE_OPTIONS,
}

# use cached template loading for performance when in production
CACHED_TEMPLATES = env('CACHED_TEMPLATES', (not DEBUG), bool)
if CACHED_TEMPLATES:
    DJANGO_TEMPLATE_OPTIONS['loaders'] = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]
else:
    DJANGO_TEMPLATES['APP_DIRS'] = True

TEMPLATES = [
    DJANGO_TEMPLATES,
]

DEFAULT_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES = env('DATABASES', DEFAULT_DATABASES, hydrate)

# internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGFILE_ROOT = env('LOGFILE_ROOT', BASE_DIR)
LOGFILE_NAME = env('LOGFILE_NAME', 'django.demo.log')
LOGFILE_PATH = env('LOGFILE_PATH', join(LOGFILE_ROOT, LOGFILE_NAME))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': (
                '[%(asctime)s] %(levelname)s '
                '[%(pathname)s:%(lineno)s] %(message)s'
            ),
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'django_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOGFILE_PATH,
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django_log_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

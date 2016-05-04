import dj_database_url
import logging
import os

SECRET_KEY = "qWsWwqfneoyzyv4dajn!=%=z3+*uswwq-$4+cj_4d&*n0@)_=-jjrthdhe@#$"

ANONYMOUS_USER_ID = -1
SITE_ID = 1
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

##################################################################
# Debug settings
##################################################################

# Set debug
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Turns on/off template debug mode.
TEMPLATE_DEBUG = DEBUG

##################################################################
# Databases settings (for docker)
##################################################################

DATABASES = {'default': dj_database_url.config()}

##################################################################
# Logging settings
##################################################################

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'

LOG_FORMATTER = logging.Formatter(
    u'%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt=LOG_DATE_FORMAT)

CONSOLE_HANDLER = logging.StreamHandler()

CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)

CONSOLE_HANDLER.setLevel(logging.DEBUG)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##################################################################
# Assets settings
##################################################################

from os.path import dirname, basename, join

SETTINGS_PATH = dirname(__file__)
PROJECT_PATH = dirname(SETTINGS_PATH)
PROJECT_NAME = basename(PROJECT_PATH)
SERVER_PATH = dirname(PROJECT_PATH)
ROOT_PATH = dirname(SERVER_PATH)

FILE_UPLOAD_PERMISSIONS = 0o644

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL
MEDIA_ROOT = join(SERVER_PATH, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = ('static',)
TEMPLATE_DIRS = ('templates',)
REDACTOR_UPLOAD = 'content/'
FLATBLOCKS_AUTOCREATE_STATIC_BLOCKS = True

##################################################################
# Finders, loaders, middleware and context processors
##################################################################

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

CORS_ORIGIN_ALLOW_ALL = True

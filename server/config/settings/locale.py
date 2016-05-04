from os.path import dirname, join

TIME_ZONE = 'Asia/Krasnoyarsk'
LANGUAGE_CODE = 'ru'

USE_I18N = True
USE_L10N = True

ugettext = lambda s: s

LANGUAGES = (
    ('ru', ugettext('Russian')),
)

LOCALE_PATHS = (
    join(dirname(dirname(__file__)), 'locale'),
)

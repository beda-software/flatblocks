
INSTALLED_APPS = (
    'adminsortable',
    'constance',
    'constance.backends.database',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'redactor',
    'flatblocks',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
    'sorl.thumbnail',
)

LOCAL_APPS = (
    'apps.blocks',
)

INSTALLED_APPS += LOCAL_APPS

MIGRATION_PATH = 'config.migrations.'


MIGRATION_MODULES = {
    'apartaments': MIGRATION_PATH + 'apartaments',
    'feedback': MIGRATION_PATH + 'feedback',
    'news': MIGRATION_PATH + 'news',
    'dbmail': MIGRATION_PATH + 'dbmail',
    'menu': MIGRATION_PATH + 'menu',
    'flatblocks': MIGRATION_PATH + 'flatblocks',
    'blocks': MIGRATION_PATH + 'blocks',
    'map': MIGRATION_PATH + 'map',
    'main': MIGRATION_PATH + 'main',
    'information': MIGRATION_PATH + 'information',
    'building_progress': MIGRATION_PATH + 'building_progress',
    'flatpages': MIGRATION_PATH + 'flatpages',
}

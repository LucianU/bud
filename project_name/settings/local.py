from {{ project_name }}.settings.common import *

DATABASES['default'].update({
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
})

# e-mail settings
DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = ''

EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

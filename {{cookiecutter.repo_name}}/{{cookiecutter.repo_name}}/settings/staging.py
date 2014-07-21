from {{ cookiecutter.repo_name }}.settings.common import *

DEBUG = False

DATABASES['default'].update({
    'NAME': '{{ cookiecutter.repo_name }}',
    'USER': '{{ cookiecutter.repo_name }}',
})

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    },
}

ALLOWED_HOSTS = [
    '.{{ domain_name }}',
]

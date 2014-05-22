"""
Django-specific tasks
"""
from fabric.api import env, task

from fabfile.helpers import virtualenv


@task
def collectstatic():
    """
    Runs collectstatic
    """
    with virtualenv():
        django_settings = 'DJANGO_SETTINGS_MODULE=%s' % env.settings
        env.run('%s ./manage.py collectstatic --noinput' % django_settings)


@task
def syncdb():
    """
    Runs syncdb (along with any pending south migrations)
    """
    with virtualenv():
        django_settings = 'DJANGO_SETTINGS_MODULE=%s' % env.settings
        env.run('%s ./manage.py syncdb --noinput' % django_settings)

"""
Helpers used with the other tasks
"""
from contextlib import contextmanager

from fabric.api import cd, env, prefix


@contextmanager
def virtualenv():
    """
    Changes to the project and activates the virtualenv
    """
    with cd(env.project):
        with prefix(env.virtualenv):
            yield

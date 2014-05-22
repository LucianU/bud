"""
Supervisor-specific tasks
"""
import os

from fabric.api import env, task

from fabfile.helpers import virtualenv


def supervisorctl(action, process):
    """
    Performs the action on the process, e.g. supervisorctl start uwsgi.
    """
    with virtualenv():
        config_file = os.path.join(env.confs, 'supervisord.conf')
        env.run('supervisorctl -c %s %s %s' % (config_file, action, process))


@task
def start_supervisord():
    """
    Starts supervisord
    """
    with virtualenv():
        config_file = os.path.join(env.confs, 'supervisord.conf')
        env.run('supervisord -c %s' % config_file)


@task
def stop_supervisord():
    """
    Restarts supervisord
    """
    with virtualenv():
        config_file = os.path.join(env.confs, 'supervisord.conf')
        env.run('supervisorctl -c %s shutdown' % config_file)


@task
def restart_supervisord():
    """
    Restarts supervisord
    """
    stop_supervisord()
    start_supervisord()

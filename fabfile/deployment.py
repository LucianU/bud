"""
Tasks useful in the deployment process
"""
import os

from fabric.api import cd, env, run, settings, sudo, task

from fabfile.django import collectstatic, syncdb
from fabfile.helpers import virtualenv
from fabfile.supervisor import start_supervisord, restart_supervisord


__all__ = ['first_deploy', 'deploy']


# Setup tasks
@task
def make_virtualenv():
    """
    Creates a virtualenv on the remote host
    """
    env.run('mkvirtualenv --no-site-packages %s' % env.virtualenv)


@task
def setup_nginx():
    """
    Uses the nginx config files to setup a virtual host
    """
    # Making a backup of the original file and then symlinking
    # our version
    sudo('mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig')
    nginx_conf = os.path.join(env.project, env.confs, 'nginx.conf')
    sudo('ln -s %s /etc/nginx/nginx.conf' % nginx_conf)

    # Simlinking the virtual host config
    site_nginx_conf = os.path.join(env.project, env.confs, 'ariseio.nginx')
    sudo('ln -s %s /etc/nginx/sites-available/ariseio' % site_nginx_conf)
    sudo('ln -s /etc/nginx/sites-available/ariseio /etc/nginx/sites-enabled/ariseio')
    sudo('service nginx reload')
#########################################################################


# Utility tasks
@task
def clone():
    """
    Clones the project from the central repository
    """
    env.run('git clone %s %s' % (env.repo, env.project))


@task
def update_code():
    """
    Pulls the latest changes from the central repository
    """
    with cd(env.project):
        env.run('git checkout %s && git pull' % env.branch)


@task
def update_reqs():
    """
    Makes sure all packages listed in requirements are installed
    """
    with virtualenv():
        env.run('pip install -r %s' % env.requirements)
#################################################################


# Shortcut tasks
@task
def first_deploy():
    """
    Sets up and deploys the project for the first time.
    """
    # If we're on the local machine, there's no point in cloning
    # the project, because it's already been cloned. Otherwise
    # the user couldn't run this file
    if env.run == run:
        # We're doing this to filter out the hosts that have
        # already been setup and deployed to
        with settings(warn_only=True):
            if env.run('test -d %s' % env.project).failed:
                return
        clone()

    # We don't setup nginx on development machines
    if env.run == run:
        setup_nginx()
    make_virtualenv()
    update_reqs()
    syncdb()
    collectstatic()

    # We don't start supervisor on development machines
    if env.run == run:
        start_supervisord()


@task
def deploy():
    """
    Deploys the latest changes to the project
    """
    update_code()
    update_reqs()
    syncdb()
    collectstatic()
    restart_supervisord()

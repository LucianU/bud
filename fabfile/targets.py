"""
Module containing tasks used to specify the deployment environment.
It also contains general settings for the project.
"""
import os

from fabric.api import env, local, run, task

env.run = run
env.repo = '/URL/OF/THE/PROJECT/REPO/'
env.virtualenv = 'workon {{ project_name }}'
env.forward_agent = True


@task
def here():
    """
    Local machine connection information
    """
    env.run = local
    env.project = os.getcwd()
    env.branch = 'master'
    env.confs = 'confs/staging/'
    env.requirements = 'requirements/staging.pip'
    env.settings = '{{ project_name }}.settings.staging'


@task
def stag():
    """
    Staging connection information
    """
    env.hosts = []
    env.project = '/ABSOLUTE/PATH/TO/WHERE/THE/PROJECT/WILL/LIVE/'
    env.branch = 'staging'
    env.confs = 'confs/staging/'
    env.requirements = 'requirements/staging.pip'
    env.settings = '{{ project_name }}.settings.staging'


@task
def prod():
    """
    Production connection information
    """
    env.hosts = []
    env.project = '/ABSOLUTE/PATH/TO/WHERE/THE/PROJECT/WILL/LIVE/'
    env.branch = 'master'
    env.confs = 'confs/production/'
    env.requirements = 'requirements/production.pip'
    env.settings = '{{ project_name }}.settings.production'

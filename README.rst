What's this?
============
With ``bud`` you can start developing a Django website in 5 minutes.


Quickstart
==========
* Install VirtualBox.

* Install vagrant.

* Install cookiecutter. You need my fork, because it supports copying without
  rendering::

    pip install git+https://github.com/LucianU/cookiecutter.git@copy-without-render

* Install ansible and passlib::

    pip install ansible passlib

* Create the ``git`` repo for your project, on GitHub, Bitbucket or any other
  service you prefer. Then copy the ``git`` URL (not ``https``).

* Create your project giving the required info when prompted. Don't worry if you
  don't have a domain name yet or other info. Later you can change what you
  enter easily by editing ``deployment/group_vars/all.yml``::

    cookiecutter https://github.com/LucianU/bud

  The prompts are::

    repo_name: the name of the project directory
    repo_url: the URL of the repo you created on GitHub, Bitbucket, etc.
    repo_host: the domain name of the repo hosting (github.com, bitbucket.org)
    ssh_private_key_path: the path to the private key you want to auth with
    webapps_root: the path to where your project will be deployed
    domain_name: the domain name of the site you're developing
    deployment_user: the name of the user created on the remote host and used
        for deployment

* Go inside your project directory and create your first commit::

    cd <project_dir>
    git init
    git add .
    git commit -m "Initial commit."

* Add the URL of the hosted repo and push the first commit::

    git remote add origin <repo_url>
    git push origin master


* Set a shortcut in ``/etc/hosts``, so that you can access your development site
  more easily::

    dev.<domain_name> 192.168.33.15

  where <domain_name> is what you entered when prompted. The domain name should
  be something like ``dog.com`` without ``www```. To know what IP to use, check
  ``Vagrantfile``.


* Boot the VM. Make sure you're in your project's directory and run::

    vagrant up

  You will see a lot of output from the boot up and the provisioning process.

* After the provisioning is done, You can access the site in the browser by
  visiting ``dev.<domain_name>``.

  .. ATTENTION::
    I recommend incrementing the IP found in ``Vagrantfile``, every time you
    start a new project. That way you wont have conflicts if you're running two
    VMs at the same time.

* When you're ready to deploy your changes to staging or production, you should
  first set the IP or name of your host in ``deployment/inventory/staging`` or
  ``deployment/inventory/production`` respectively. This machine should be
  accessible through password authentication

* Then you need to run a command that will prepare the machine::

    ansible-playbook deployment/secure.yml -kK -u <user>

  Where ``<user>`` is the user you login as. This user should have sudo rights.
  You will be prompted for the password of this user and also for the password
  of the deployment user that will be created.

* Let's say you prepared this machine for staging. After the previous command
  finished, you can deploy the site by running::

    ansible-playbook deployment/staging.yml -K


How It Works
============
``bud`` relies on ``cookiecutter`` to populate the project files with the
information that you provide when you are prompted. Then it relies on
``vagrant`` to manage VMs and ``ansible`` to provision your hosting machine and
deploy your site to it. ``bud`` assumes the following stack for the Django
site::

    64-bit Ubuntu Server 12.04
    git
    PostgreSQL
    nginx
    memcached
    uwsgi
    supervisor


Overview
========
There two main things you need to understand: the layout of the project and the
layout of the ``deployment`` directory.

Project layout
--------------
The layout of the project is::

    project
    |--ansible.cfg
    |--LICENSE
    |--manage.py
    |--README.rst
    |--Vagrantfile
    |--deployment/
       |--...
    |--requirements/
       |--common.pip
       |--development.pip
       |--production.pip
    |--project/
       |--__init__.py
       |--urls.py
       |--wsgi.py
       |--apps/
          |--globe/
             |--__init__.py
             |--models.py
             |--tests.py
             |--views.py
       |--settings/
          |--__init__.py
          |--common.py
          |--development.py
          |--local.py
          |--production.py
          |--staging.py
       |--static/
          |--css/
             |--main.css
          |--img/
             |--favicon.ico
          |--js/
             |--main.js
       |--templates/
          |--404.html
          |--500.html
          |--base.html


Requirements
^^^^^^^^^^^^
There are 3 requirements files. The production requirements file is used for
staging as well.

Apps
^^^^
The ``apps`` directory is where you keep your apps. This directory is included
in the Python path, so imports from an app start with the name of that app. For
example, to import from the views of the ``globe`` app, you write::

    from globe.views import ...

The ``globe`` app found in the ``apps`` directory is a global app. You should
put here code that is relevant to your whole project and not a single app. For
example, if you have mixins that aren't specific to a particular app, you should
put them in the ``globe`` app.

Settings
^^^^^^^^
The settings are also split into several files, one for each deployment target.
There is another file called ``local.py`` which is ignored by ``git``. You can
use it for settings that you don't want version controlled like your GMail
credentials.

In this directory there is another file that will only appear in the generated
project. If you open ``settings/common.py``, you only notice that ``SECRET_KEY``
is imported from ``settings.secure``. The ``settings/secure.py`` file is
generated by ``cookiecutter``.

``deployment`` layout
---------------------
The layout is::

    deployment
    |--development.yml
    |--production.yml
    |--secure.yml
    |--staging.yml
    |--group_vars/
       |--all.yml
       |--development.yml
       |--production.yml
       |--staging.yml
    |--host_vars/
    |--inventory/
       |--development
       |--production
       |--staging
    |--roles/
       |--common/
          |--files/
             |--...
          |--handlers/
             |--...
          |--tasks/
             |--...
          |--templates/
             |--...
          |--vars/
             |--...
       |--memcached/
          |--...
       |--nginx/
          |--...
       |--postgres/
          |--...
       |--secure/
          |--...
       |--site/
          |--...
       |--supervisor/
          |--...
       |--uwsgi/
          |--...
       |--virtualenv/
          |--...

The first thing you care about is the ``inventory`` directory. Here you set the
IP or domain name of your hosts. You can check that ``inventory/development``
contains the same IP as the one in ``Vagrantfile``. In the other two files, you
need to change the values with those of your hosts.

The ``roles`` directory contains `Ansible Roles`_. As you can probably deduce
from the names of the roles, a role has a specific purpose. The ``nginx`` role
installs and configures ``nginx``. If you wanted to start using ``SOLR`` in your
project, you would add a ``solr`` role.

The YAML files found directly in ``deployment`` contain `Ansible Playbooks`_. A
playbook specifies which roles or tasks to run against which host. If you've
added a ``solr`` role, you should also add it in the playbooks here, to make sure
it will run.

Another important directory is ``group_vars``. This contains variables used
throught the project. The ``all.yml`` file contains variables that apply to all
hosts, while in the other files you can override these variables. Notice that
you can reference a variable when setting another one, which is a very useful
feature. To know the valid names and syntax, you can read about `Ansible
Variables`_.

.. _`Ansible Roles`: http://docs.ansible.com/playbooks_roles.html#roles
.. _`Ansible Playbooks`: http://docs.ansible.com/playbooks_intro.html
.. _`Ansible Variables`: http://docs.ansible.com/playbooks_variables.html

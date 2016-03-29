# bud
`bud` provides automation for your Django site. You create a project from
`bud` and you get automated setup for development and for deployments. `bud`
uses Vagrant and Ansible to provide this functionality. Because `bud` follows
[12 factor app](http://12factor.net/) guidelines, you'll be using
industry best practices.

`bud` assumes the following stack:
- Ubuntu
- PostgreSQL
- Memcached
- Nginx
- uWSGI
- Git

# Features:
- provides automated management of a development environment through Vagrant
- provides automated provisioning and deployment through Ansible
- integrates with `django-environ`. This makes it easy to set configuration
through environment variables.
- uses `django-allauth` for authentication
- provides an Ansible role that hardens your server against common attacks

# Setup
- Install VirtualBox, Vagrant and pip.
- Install the necessary Python libs:

    pip install ansible cookiecutter passlib

- Create the project:

    cookiecutter https://github.com/lucianu/bud

  You will receive the following prompts:

    - `project_name`: the name of the project directory
    - `deployment_user`: the name of the user created on the remote host and used for deployment
    - `ssh_private_key_path`: the path to the private key you want to auth with

- Go inside the project and run `vagrant up`
- After the setup finishes, you can go to `http://localhost:8000` and you'll
see the default Django starting page.

# `bud` vs Django default project
`bud` adds to the default Django project the following:
- a `users` app that comes with a custom `User` model and adapters for
`django-allauth`'s authentication.
- an `apps` dir to make visible the distinction between project and apps code
- a `templates` dir that contains a base template and templates for 404 and 5xx
errors.
- a `static` dir for static files.
- settings integration with `django-environ`.


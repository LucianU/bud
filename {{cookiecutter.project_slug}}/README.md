# About
Describe the project

# Setup
* Install `docker` and `docker-compose`. On Mac, you can do that with:
  `brew cask install docker`

* To start the development environment, run
  `./bin/start-dev-env`

* To stop the development environment, run in a different terminal:
  `./bin/stop-dev-env`

# Functionality
## Authentication
Provided by `django-allauth`

## Static files
Disabled by default. To enable support for static files, set in `env_files/development/.env`
`DJANGO_ENABLE_STATIC_FILES=True`.

Using `whitenoise` to  serve static files.

## Emails
Managed with `django-anymail`.

# To Do
* Add `browser-app` dir under `templates` and put `index.html` in there.
* Document common `manage.py` operations like `makemigrations` and `startapp`.
* Document `env_files`.

# About
Describe the project

# Setup
* Install `docker` and `docker-compose`
* To start the development environment, run
  `./scripts/start-local`

* To stop the development environment, run in a different terminal:
  `./scripts/stop-local`

# Functionality
## Authentication
Provided by `django-allauth`

## Static files
Disabled by default. To enable support for static files, set in `env_files/local/.env`
`DJANGO_ENABLE_STATIC_FILES=True`.

Using `whitenoise` to  serve static files.

## Emails
Managed with `django-anymail`.

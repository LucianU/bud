# What is this?
Another Django project template. Heavily inspired by
[Cookiecutter](https://github.com/cookiecutter/cookiecutter)'s Django template.

# Features
- manages the development environment with `docker-compose`
- uses `pre-commit` to prevent you from committing unfit code
- uses `mypy` for type-checking
- uses `black` to format the code
- uses `EditorConfig` for consistent editing experience
- uses `django-configurations` to follow the 12-factor-app guidelines. There is a single settings.py
and you can override settings with environment variables.
- uses PostgreSQL as the database
- uses Redis for caching
- uses `browser_app` for project-specific code. No more global `static` and `templates` directories.

# How to use
- Since this is a cookiecutter template, we use that to generate a project from
  this template:

  ```sh
  pipx run cookiecutter path/to/bud
  ```


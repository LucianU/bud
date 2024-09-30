# Archived
Since I don't use Django much, I don't need a starter project.

# What is this?
Another Django project template. Heavily inspired by Cookiecutter's Django template.

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

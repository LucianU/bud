#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line


if __name__ == "__main__":
    # Making sure we can import each app
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(PROJECT_ROOT, '{{ cookiecutter.repo_name }}/apps'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.repo_name }}.settings")
    execute_from_command_line(sys.argv)

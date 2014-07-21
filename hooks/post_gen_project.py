#!/usr/bin/env python

"""
Generates a Python file with the secret key needed by Django.
"""

import os
import random
import string


def generate_secret_key():
    choices = string.digits + string.letters + string.punctuation
    return "".join(random.SystemRandom().choice(choices) for i in xrange(100))


def generate_file():
    project_name = os.path.basename(os.getcwd())
    file_path = os.path.join(os.getcwd(), project_name, 'settings', 'secret.py')
    with open(file_path, 'w') as f:
        file_content = 'SECRET_KEY=%s' % generate_secret_key()
        f.write(file_content)


if __name__ == '__main__':
    generate_file()

#!/usr/bin/env python

"""
Generates a Python file with the secret key needed by Django.
"""

import os
import random


def generate_secret_key(length):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return "".join(random.SystemRandom().choice(chars) for i in xrange(length))


def main():
    project_name = os.path.basename(os.getcwd())
    file_path = os.path.join(os.getcwd(), project_name, '.env')
    with open(file_path, 'r+') as f:
        file_content = f.read()
        file_content %= generate_secret_key(50)

        # We overwrite the contents of the file
        f.seek(0)
        f.write(file_content)


if __name__ == '__main__':
    main()

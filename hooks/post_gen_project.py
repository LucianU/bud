#!/usr/bin/env python

"""
Generates a Python file with the secret key needed by Django.
"""
# import os
# import random
# import shutil
# import string
# def remove_docker_files():
#     shutil.rmtree("compose")
#
#     file_names = ["local.yml", "production.yml", ".dockerignore"]
#     for file_name in file_names:
#         os.remove(file_name)
#
#
# def remove_utility_files():
#     shutil.rmtree("utility")
#
# if "{{ cookiecutter.GIS_project }}".lower() == "y":
#         remove_utility_files()
#     else:
#         remove_docker_files()
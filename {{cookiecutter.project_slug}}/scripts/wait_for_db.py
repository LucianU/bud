#!/usr/bin/env python3

"""
This utility script checks if the PostgreSQL database is ready for use.
"""

import logging
import os
import sys
from time import sleep, time
from django.conf import settings

import psycopg2

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


if __name__ == "__main__":
    config = {
        # These are currently set in the .env file
        "dbname": os.environ.get("DJANGO_DATABASES_NAME"),
        "user": os.environ.get("DJANGO_DATABASES_USER"),
        "host": os.environ.get("DJANGO_DATABASES_HOST"),
        "port": os.environ.get("DJANGO_DATABASES_PORT"),
    }

    start_time = time()
    timeout = 30
    while time() - start_time < timeout:
        try:
            conn = psycopg2.connect(**config)
            logger.info("DB ready! 🎉")
            conn.close()
            sys.exit()
        except psycopg2.OperationalError:
            logger.info(f"DB not ready. Waiting for 1 second ...")
            sleep(1)

    logger.error(f"Could not connect to DB within {timeout} seconds.")

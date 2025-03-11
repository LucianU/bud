#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


python bin/wait_for_db.py &&\
python manage.py migrate &&\
python manage.py runserver 0.0.0.0:8000

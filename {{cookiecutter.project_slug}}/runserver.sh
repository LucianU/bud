#!/usr/bin/env bash

export DJANGO_SECRET_KEY="*8e+^@x8rs%4jp1blufis93um_1a=k%(63p%6i*6o((6xr6^5@"
{% if cookiecutter.GIS_project == "y" %}
export DJANGO_GDAL_LIBRARY_PATH="/nix/store/iqqv4ivbf1yrzzp3sypfj8w7q6jvqm1l-gdal-2.4.0/lib/libgdal.so"
export DJANGO_GEOS_LIBRARY_PATH="/nix/store/3rp5scw6b18g9ya0vw0mh1rp6r2r2qwb-geos-3.7.1/lib/libgeos_c.so"
{% endif %}

./manage.py migrate
./manage.py collectstatic --no-input
./manage.py runserver 0.0.0.0:8000


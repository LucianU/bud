#!/usr/bin/env bash

docker-compose -f ./development.yml run --rm web python manage.py "$@"

#!/usr/bin/env bash

docker-compose -f ./local.yml run --rm web python manage.py "$@"

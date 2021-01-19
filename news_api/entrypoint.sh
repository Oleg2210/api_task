#!/bin/bash
while ! nc -z $POSTGRES_HOSTNAME $POSTGRES_PORT; do
  sleep 0.2
done

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 project.wsgi

#!/bin/bash

echo "Collect static files"
python3 manage.py collectstatic --noinput

echo "Apply database migrations"
python3 manage.py migrate

echo "Starting server"
gunicorn --chdir ideablog --bind :8005 --timeout 300 ideablog.wsgi:application

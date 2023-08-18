#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    # while ! nc -z $SQL_HOST $SQL_PORT; do
    #   sleep 0.1
    # done
    sleep 10

    echo "PostgreSQL started"
fi

echo "Collect static files"
python3 manage.py collectstatic --noinput

echo "Apply database migrations"
python3 manage.py migrate

echo "Starting server"
gunicorn --chdir ideablog --bind :8005 --timeout 300 ideablog.wsgi:application


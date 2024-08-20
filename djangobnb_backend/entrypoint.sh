#!/bin/sh

if [ "$DATABASE" = "postgres" ] 
then
    echo "Waiting for PostgreSQL to start..."

    echo "Using SQL_HOST: $SQL_HOST and SQL_PORT: $SQL_PORT"

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
        sleep 1
    done

    echo "PostgreSQL is up and running :-D"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"

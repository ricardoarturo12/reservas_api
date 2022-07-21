#!/bin/sh
while ! python manage.py makemigrations 2>&1; do
    echo  "makemigrations "
    sleep 3
done

while ! python manage.py migrate 2>&1; do
    echo "migrate"
    sleep 3
done
exec "$@"
#!/bin/sh

set -e
export DJANGO_SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
echo ${DJANGO_SECRET_KEY}
python manage.py makemigrations
python manage.py migrate
#python manage.py collectstatic --noinput
uwsgi --socket :8000 --master --enable-thread --module app.wsgi

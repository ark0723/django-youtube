#!/bin/sh
# 오류가 발생하면 알려줘 :set -e
set -e 

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

# uWSGI: Nginx로부터 데이터를 받아오면 Django랑 소통을 하는 역활
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
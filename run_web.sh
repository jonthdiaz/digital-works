#!/bin/sh

#alias python to python3.4
echo "[alias python]"
alias python=/usr/bin/python3.4

#cd digital-works
echo "[cd digital-works]"
cd /digital-works

#migrate db, so we have the latet db schema
echo "[manage.py migrate]"
python manage.py migrate

echo "[run] create superuser"
echo "from django.contrib.auth.models import User
if not User.objects.filter(username='dwadmin').count():
        User.objects.create_superuser('dwadmin', 'jonthdiaz@gmail.com', 'dwadmin')
        " | python manage.py shell

#start development server on public ip interface, on port 8080
echo "[runserver]"
python manage.py runserver 0.0.0.0:8080 --settings=dw.local_settings

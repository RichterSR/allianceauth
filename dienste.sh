#! /bash/sh
cd /home/allianceserver/allianceauth
screen -dm bash -c 'python manage.py celeryd --verbosity=2 --maxtasksperchild=250 --loglevel=DEBUG'
screen -dm bash -c 'python manage.py celerybeat --verbosity=2 --loglevel=DEBUG'
pyhton manage.py runserver 0.0.0.0:8000

#!/bin/bash
sudo /bin/mkdir /var/log/sparky
sudo /usr/bin/touch /var/log/sparky/debug.log
sudo chmod -R ugo+rw /var/log/sparky

sudo ufw allow 44444
sudo ufw allow 7070
sudo apt  -y install default-libmysqlclient-dev mysql-server

# CREATE USER django;
# CREATE DATABASE DB1 CHARACTER SET utf8;
# GRANT ALL PRIVILEGES ON DB1.* TO 'django'@'localhost' WITH GRANT OPTION;

virtualenv -p python2 testa
source testa/bin/activate


pip install -r requirements.txt

./manage.py makemigrations
./manage.py migrate
# ufw allow 7070
./manage.py runserver 0.0.0.0:7070 &

sleep 2s

python server.py &

sleep 2s

python atm.py
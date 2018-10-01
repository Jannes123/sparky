#!/bin/bash
sudo /bin/mkdir /var/log/sparky
sudo /usr/bin/touch /var/log/sparky/debug.log
sudo chmod -R ugo+rw /var/log/sparky


virtualenv -p python2 testa
source testa/bin/activate

pip install -r requirements.txt

./manage.py makemigrations
./manage.py migrate
# ufw allow 7070
./manage.py runserver 0.0.0.0:7070 &

python server.py &
python atm.py
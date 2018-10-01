#!/usr/bin/python
import socket
import os
import django
from sink.models import Messages
django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sparky.settings")

import logging
import logging.config
from sparky.settings import LOGGING
logging.config.dictConfig(LOGGING)
LOGGER = logging.getLogger('sink')

s = socket.socket()
host = socket.gethostname()
port = 44444
s.bind((host, port))

s.listen(5)
while True:
   c, addr = s.accept()
   LOGGER.debug('Got connection from ' + str(addr))
   payload = c.recv(1024)
   LOGGER.debug('received ' + str(payload))
   m = Messages.objects.create(source=addr, payload=payload)
   c.send('ACK')
   c.close()

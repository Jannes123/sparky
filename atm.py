#!/usr/bin/python
import socket
import logging
import logging.config
import random
from sparky.settings import LOGGING

logging.config.dictConfig(LOGGING)
LOGGER = logging.getLogger('sink')

host = socket.gethostname()  # Get local machine name
port = 44444                 # Reserve a port for your service.

LOGGER.debug('start ATM')

def send_message_one():
    """
    Send Configuration message and logs to db
    :return: boolean
    """
    s1 = socket.socket()
    s1.connect((host, port))
    s1.send("...config1..." + str(random.randint(1, 10001)))
    LOGGER.debug('sent config..receiving.. ' + str(s1.recv(1024)))
    s1.close()


def send_message_two():
    """
    Send Health message and logs to db
    :return: boolean
    """
    s1 = socket.socket()
    s1.connect((host, port))
    s1.send('...HELATH 100...')
    LOGGER.debug('sent health..receiving.. ' + str(s1.recv(1024)))
    s1.close()

if __name__ == '__main__':
    for i in range(1,11):
        send_message_one()
        send_message_two()
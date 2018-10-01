# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Messages(models.Model):
    """
    Represents database scheme to log ATM messages to mysql db
    """
    source = models.CharField(max_length=100)
    payload = models.CharField(max_length=100)

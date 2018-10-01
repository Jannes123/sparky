# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Messages
from django.views.generic import ListView


class ViewListPost(ListView):
    queryset = Messages.objects.all()
    template_name = 'list.html'


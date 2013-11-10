# -*- coding: utf-8 -*-
'''
Created on 18 oct 2013

@author: franck
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from movesevent.models.movesUser import MovesUser
import logging
from movesevent.models.movesApp import MovesApp

logger=logging.getLogger("mvevt")

logger.debug("%s loaded" , __name__)
admin.site.register(MovesUser)
admin.site.register(MovesApp)
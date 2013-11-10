# -*- coding: utf-8 -*-
'''
Created on 7 nov 2013

@author: franck
'''

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

        
class MovesApp(models.Model):    
    """
    Moves App Identifier, id and secret
    """

    app_name = models.CharField(_(u"Application name"), unique=True, max_length=50, null=True, blank=True)
    """
    Moves application name
    """

    last_modified = models.DateTimeField(_(u"Last modification date"), auto_now=True, blank=True) # Automatic import date
    created_date = models.DateTimeField(_(u"Creation date"),auto_now_add=True, blank=True)
    
    client_id     = models.CharField(max_length=150, null=True, blank=True)
    """
    the Client ID your received when registering your application
    """

    client_secret = models.CharField(max_length=150, null=True, blank=True)
    """
    the Client Secret your received when registering your application
    """
        
    def __unicode__(self):
        return '%s ' % (self.app_name);
    
        
    # Cela semble obligatoire pour la generation de la base
    class Meta:
        app_label='movesevent'
        verbose_name = "Moves application profile"
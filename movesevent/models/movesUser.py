# -*- coding: utf-8 -*-
'''
Created on 18 oct 2013

@author: franck
'''

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from movesevent.models.movesApp import MovesApp

        
class MovesUser(models.Model):    
    """
    Moves user profile.
    """
    user = models.ForeignKey(User)
    app = models.ForeignKey(MovesApp)
    
    last_modified = models.DateTimeField(_(u"Last modification date"), auto_now=True, blank=True) # Automatic import date
    created_date = models.DateTimeField(_(u"Creation date"),auto_now_add=True, blank=True)
    
    access_token = models.CharField(max_length=255, null=True, blank=True)
    """
    Moves access token
    """
        
    def __unicode__(self):
        return '%s/%s' % (self.user.username, self.app.app_name);
    
        
    # Cela semble obligatoire pour la generation de la base
    class Meta:
        app_label='movesevent'
        unique_together = (("user", "app"),)
        verbose_name = "Moves user"
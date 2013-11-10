# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck
'''
from django.contrib.auth.models import User
from movesevent.models.movesUser import MovesUser
import logging


logger = logging.getLogger("mvevt")

def get_moves_users(user_id):
    """
    Return the corresponding moves users
    None if missing
    """
    try:
        user= User.objects.get(id=user_id)
        move_user=user.movesuser_set
    except (MovesUser.DoesNotExist, User.DoesNotExist):
        logger.warn("unknown moves user %d", user_id)
        move_user=None
    return move_user

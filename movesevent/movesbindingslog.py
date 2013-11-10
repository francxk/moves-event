# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck
'''
from django.dispatch.dispatcher import receiver
import logging
from movesevent.signal import moves_place, moves_activity, moves_move
import pprint


# get a logger
logger = logging.getLogger('mvevt.evt')
logger.debug("%s loaded " % __name__)
_lvl=5

class Lazy(object):
    """
    Lazy call for logger
    """
    def __init__(self,func):
        self.func=func
    def __str__(self):
        return self.func()

if logger.isEnabledFor(_lvl):
    @receiver(moves_place)
    def moves_place_logger(sender, **kwargs):
        logger.log(_lvl, "place\n%s", Lazy(lambda : pprint.pformat(kwargs["place"])))
    
    @receiver(moves_activity)
    def moves_activity_logger(sender, **kwargs):
        logger.log(_lvl, 
                     """\n-----------------Activity--------------
    %s
    ---------------------------------------""", Lazy(lambda : pprint.pformat(kwargs["activity"])))
    
    @receiver(moves_move)
    def moves_move_logger(sender, **kwargs):
        logger.log(_lvl, "move\n%s", Lazy(lambda : pprint.pformat(kwargs["move"])))

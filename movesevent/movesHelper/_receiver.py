#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 28 oct. 2013

@author: franck
'''
from movesevent.signal import moves_place, moves_activity, moves_move,\
    moves_summary
import logging

logger=logging.getLogger("mvevt")

logger.debug("%s loaded", __name__)

class MovesReceiver(object):
    '''
    Move signal receiver.
    overide to your usage
    '''

    def __init__(self, movesuser,catch_moves_place=False, catch_moves_activity=False,
                 catch_moves_move=False, catch_moves_summary=False, sender=None):
        '''
         Choose which receiver you need.
        '''
        self.user=movesuser.user
        self.move_user=movesuser
        if catch_moves_place: moves_place.connect(self.on_moves_place,sender=sender)
        if catch_moves_activity: moves_activity.connect(self.on_moves_activity,sender=sender)
        if catch_moves_move: moves_move.connect(self.on_moves_move,sender=sender)
        if catch_moves_summary: moves_summary.connect(self.on_moves_summary,sender=sender)
        
    def on_moves_place(self, sender, **kwargs):
        logger.debug("on_moves_place %s", kwargs["place"]["place"].get("name", 'unk'))
        
    def on_moves_activity(self, sender, **kwargs):
        logger.debug("on_moves_activity")
        
    def on_moves_move(self, sender, **kwargs):
        logger.debug("on_moves_move")
        
    def on_moves_summary(self, sender, **kwargs):
        logger.debug("on_moves_summary")
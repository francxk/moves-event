# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck
'''
from moves import MovesClient
import logging
from movesevent import signal

logger = logging.getLogger("mvevt")


class MovesEventDispatcher(object):
    """
    Send event for story line...
    Sender is the moves user
    """
    def __init__(self, moves_user):
        self.moves_user = moves_user
        self.movesApi= None
        self._initMovesApi()


    def _initMovesApi(self):
        """
        Init moves Api Client
        """
        if self.movesApi:
            del self.movesApi
        self.movesApi = MovesClient(self.moves_user.app.client_id,
                                    self.moves_user.app.client_secret)
    
    def moves_storyline(self, **kwargs):
        '''
        Get moves user story lines.
        Same parameter as moves API. see docs
        '''
        logger.debug("story_lines for %s", self.moves_user.user.username)
        story_line = self.movesApi.user_storyline_daily(access_token=self.moves_user.access_token,
                                                        **kwargs)
        return story_line
    
    def _place_handler(self, place):
        logger.debug(" place handling %s", place["place"].get("name", 'unk'))
        signal.moves_place.send(sender=self.moves_user, moves_user= self.moves_user, place=place)
        if "activities" in place:
            for activity in place["activities"]:
                signal.moves_activity.send(sender=self.moves_user, moves_user= self.moves_user,
                                           place=place,
                                           activity=activity)
    
    def _move_handler(self, move):
        logger.debug(" move handling ")
        signal.moves_move.send(sender=self.moves_user, moves_user= self.moves_user, move=move)
        if "activities" in move:
            for activity in move["activities"]:
                signal.moves_activity.send(sender=self.moves_user, moves_user= self.moves_user,
                                           move=move,
                                           activity= activity)
        
    
    __main_handlers = {"place": _place_handler, "move": _move_handler}
    
    def moves_dispatch_storyline_events(self, **kwargs):
        logger.debug('dispatch storyline event for %s ', self.moves_user.user.username)
        story_line = self.moves_storyline(**kwargs)
        for day in story_line:
            logger.debug("%s ", day["date"])
            for segment in day["segments"]:
                handler=self.__main_handlers.get(segment["type"])
                if handler:
                    handler(self,segment)
                else:
                    logger.error("Unkown segment type %s", segment["type"])
            
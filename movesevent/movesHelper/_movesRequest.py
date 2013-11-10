# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck
'''
from moves import MovesClient, MovesAPIError
import logging
from django.core.urlresolvers import reverse
from django.http.request import HttpRequest

from movesevent import signal

logger = logging.getLogger("mvevt")


class MovesAPIAccessTokenMissing(MovesAPIError):
    def __init__(self,*args, **kwargs):
        super(MovesAPIAccessTokenMissing, self).__init__(*args)
        self.webapp = kwargs.get('webapp', None)


def access_token_protect(movesApi,request, user_id):
    '''
    If func if not ok, suppose that is a pb of access_token and give the MovesAPIAccessTokenMissing exception.
    Can be use around moves API.
    '''
    def access_token_protector(func):
        def wrapper(*args, **kwargs):
            logger.debug(" tok protect %s", func.__name__)
            try:
                res = func(*args,**kwargs)
            except MovesAPIError, e:
                logger.debug("api error %s", e)
                oauth_return_url = reverse('oauth_return', args=(user_id,))
                if request:
                    full_uri = HttpRequest.build_absolute_uri(request, oauth_return_url)
                    auth_url = movesApi.build_oauth_url(full_uri)
                else:
                    auth_url = None
                raise MovesAPIAccessTokenMissing(e, webapp=auth_url)
            finally:
                logger.debug(" tok protect endind %s", func.__name__)
            return res
        return wrapper
    return access_token_protector


def access_token_protector(func):
    '''
    access_tocken_protector decorator for class    
    '''
    def wrapper(self, *args, **kwargs):
        return access_token_protect(self.movesApi, self.request, self.moves_user.id)(func)(self,*args,**kwargs)
    return wrapper
     
class MovesEventDispatcher(object):
    """
    Send event for story line...
    Sender is the moves user
    """
    def __init__(self, moves_user, current_request = None):
        self.moves_user = moves_user
        self.movesApi= None
        self._initMovesApi()
        self.request = current_request


    def _initMovesApi(self):
        """
        Init moves Api Client
        """
        if self.movesApi:
            del self.movesApi
        self.movesApi = MovesClient(self.moves_user.app.client_id,
                                    self.moves_user.app.client_secret)
    from django.http.request import HttpRequest

    @access_token_protector
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
            
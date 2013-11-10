# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck
'''
import logging
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse, Http404
from movesevent.models.movesUser import MovesUser
from moves import MovesClient,MovesAPINotModifed,MovesAPIError
from django.core.urlresolvers import reverse
from django.http.request import HttpRequest
from requests.exceptions import HTTPError
import datetime
from movesevent.movesHelper import MovesEventDispatcher, MovesAPIAccessTokenMissing
import traceback
from movesevent.movesHelper._movesRequest import access_token_protect

logger=logging.getLogger("mvevt")

logger.debug("%s loaded", __name__)

def sync4user(request,user_id):
    logger.debug("refresh4user %s", user_id)
    user_id = int(user_id)
    try:
        move_user = MovesUser.objects.get(id=user_id)
    except (MovesUser.DoesNotExist, User.DoesNotExist):
        logger.warn("unknown moves user %d", user_id)
        raise Http404(_(u"unknown moves user %d")% user_id)
    mv_dsp = MovesEventDispatcher(move_user,request)
    movesApi = mv_dsp.movesApi
    logger.debug("start etag = %s", movesApi.etag)
    
    try:
        logger.debug("before etag = %s", movesApi.etag)
        profile = access_token_protect(movesApi, request, user_id)(movesApi.user_profile) (access_token=move_user.access_token)
        logger.debug("%s", profile)
        logger.debug("etag = %s", movesApi.etag)
        date1= datetime.datetime.now() - datetime.timedelta(days=3  )
        date_range= { 'from':date1.strftime("%Y%m%d"), 'to':date1.strftime("%Y%m%d"), 'trackPoints':'true'}
    #    date_range= { 'from':'20131018', 'to':'20131018', 'trackPoints':'true'}
        mv_dsp.moves_dispatch_storyline_events(**date_range)
        logger.debug("etag = %s", movesApi.etag)
        logger.debug("refresh4user ended")
    except MovesAPIAccessTokenMissing, e:
        return HttpResponse('Authorize this application: <a href="%s">%s</a>' % \
            (e.webapp, e.webapp))
    except MovesAPIError, e:
        logger.debug("api error %s", traceback.format_exc())
        raise e

    except MovesAPINotModifed, e:
        logger.debug("No change on profile")
    
    return HttpResponse("OK")

def oauth_return(request,user_id):
    """
    Return here to get and register access token
    """
    logger.debug("oauth_return %s" , user_id)
    user_id = int(user_id)
    try:
        move_user = MovesUser.objects.get(id=user_id)
    except (MovesUser.DoesNotExist, User.DoesNotExist):
        logger.warn("unknown moves user %d", user_id)
        raise Http404(_(u"unknown moves user %d")% user_id)

    error = request.GET.get('error', None)
    if error is not None:
        logger.error("Move OAuth Error %s", error)
        raise HTTPError(_(u"Move OAuth Error %s"% error))
                          
    movesApi = MovesClient(move_user.app.client_id, move_user.app.client_secret)
    
    code = request.GET.get("code",None)
    oauth_return_url = reverse('oauth_return', args=(user_id,))
    full_uri = HttpRequest.build_absolute_uri(request, oauth_return_url)
    token = movesApi.get_oauth_token(code, redirect_uri=full_uri)
    
    move_user.access_token = token
    move_user.save()
    
    return redirect(reverse('syncuser', args=(user_id,)))
    
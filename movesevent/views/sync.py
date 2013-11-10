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
from moves import MovesClient,MovesAPINotModifed
from django.core.urlresolvers import reverse
from django.http.request import HttpRequest
from requests.exceptions import HTTPError
import datetime
from movesevent.movesHelper import MovesEventDispatcher

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
    mv_dsp = MovesEventDispatcher(move_user)
    movesApi = mv_dsp.movesApi
    logger.debug("start etag = %s", movesApi.etag)
    
    if move_user.access_token == None or move_user.access_token=='':
        oauth_return_url = reverse('oauth_return', args=(user_id,))
        full_uri = HttpRequest.build_absolute_uri(request, oauth_return_url)
        logger.info(" Ask authorisation for user %d", user_id)
        auth_url = movesApi.build_oauth_url(full_uri)
        return HttpResponse('Authorize this application: <a href="%s">%s</a>' % \
            (auth_url, auth_url))

    try:
        logger.debug("before etag = %s", movesApi.etag)
        profile = movesApi.user_profile(access_token=move_user.access_token)
        logger.debug("etag = %s", movesApi.etag)
        logger.debug("%s", profile)
    except MovesAPINotModifed, e:
        logger.debug("No change on profile")
    date1= datetime.datetime.now() - datetime.timedelta(days=3  )
    date_range= { 'from':date1.strftime("%Y%m%d"), 'to':date1.strftime("%Y%m%d"), 'trackPoints':'true'}
#    date_range= { 'from':'20131018', 'to':'20131018', 'trackPoints':'true'}
    mv_dsp.moves_dispatch_storyline_events(**date_range)
    logger.debug("etag = %s", movesApi.etag)
    logger.debug("refresh4user ended")
    
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
    
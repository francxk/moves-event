# -*- coding: utf-8 -*-
'''
Created on 20 oct. 2013

@author: franck
'''
import django.dispatch

'''
Moves events
'''

moves_place = django.dispatch.Signal(providing_args=["moves_user", "places",])
'''
Send when user stay in places.
place has the format:
{u'place': {u'type': u'unknown', u'id': 147236385,
 u'location': {u'lat': 45.25732, u'lon': 5.86234}},
 u'endTime': u'20131018T225316Z', u'type': u'place', u'startTime': u'20131018T215700Z',
 u'activities': [{u'distance': 7.0, u'calories': 0, u'steps': 14,
                 u'startTime': u'20131018T225255Z', u'activity': u'wlk',
                 u'duration': 20.0, u'endTime': u'20131018T225315Z'}]}

'''

moves_activity = django.dispatch.Signal(providing_args=["moves_user","activity",])
''' Send when user made an activity.
signal has a place or a move as parameter
{u'activity': u'wlk',
 u'calories': 2,
 u'distance': 46.0,
 u'duration': 60.0,
 u'endTime': u'20131019T212408Z',
 u'startTime': u'20131019T212308Z',
 u'steps': 91}
'''

moves_move = django.dispatch.Signal(providing_args=["moves_user","move",])
''' Send when user moves'''

moves_summary = django.dispatch.Signal(providing_args=["moves_user","summary",])
''' Send when summary is requested'''


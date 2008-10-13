#
# Copyright 2008, BlueDynamics Alliance, Austria - http://bluedynamics.com
#
# Zope Public License (ZPL)
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL). A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plain'

from zope.interface import implements
from zope.component import adapts
from zope.component import queryAdapter
from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.http import IHTTPRequest
from Acquisition import aq_inner
from cornerstone.feed.core.interfaces import IFeed

class FeedTraverser(object):
    """Used to traverse to a IFeed 
    """
    implements(ITraversable)
    
    def __init__(self, context, request=None):
        self.context = context
        self.request = request
        
    def traverse(self, name, ignore):
        print name
        feed = queryAdapter(self.context, IFeed)
        if feed is None:
            raise AttributeError, "No feed factory found!"
        feed = feed.__of__(aq_inner(self.context))
        return feed
       
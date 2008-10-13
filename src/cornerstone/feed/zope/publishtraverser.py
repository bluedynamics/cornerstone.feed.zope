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
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.publisher.interfaces.browser import IBrowserPublisher
from ZPublisher.BaseRequest import DefaultPublishTraverse
from Acquisition import aq_inner
from cornerstone.feed.core.interfaces import IFeed
from feedgenerator import ZopeFeedGenerator

class FeedPublishTraverse(DefaultPublishTraverse):
    """The traverser for the feed representation itself.
    """
    implements(IBrowserPublisher)
    adapts(IFeed, IDefaultBrowserLayer)
    
    def publishTraverse(self, request, name):            
        generator = ZopeFeedGenerator(self.context, name, request)
        generator = generator.__of__(aq_inner(self.context))
        return generator
        
        

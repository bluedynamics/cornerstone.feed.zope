# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

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
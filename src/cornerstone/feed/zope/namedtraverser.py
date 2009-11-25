# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

from zope.interface import implements
from zope.component import adapts
from zope.component import queryAdapter
from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.http import IHTTPRequest
from Acquisition import aq_inner
from cornerstone.feed.core.interfaces import IFeed

class FeedTraverser(object):
    """Used to traverse to a IFeed. 
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
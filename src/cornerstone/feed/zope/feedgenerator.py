# Copyright 2008-2009, BlueDynamics Alliance - http://bluedynamics.com
# Zope Public License (ZPL)

from Acquisition import Explicit
from cornerstone.feed.core.feedgenerator import FeedGenerator

class ZopeFeedGenerator(FeedGenerator, Explicit):
    
    def __init__(self, feed, name, request):
        FeedGenerator.__init__(self, feed, name)
        self.request = request
    
    def __call__(self):
        data, mimetype = self.generate()
        if mimetype is not None:
            self.request.response.setHeader('Content-Type', mimetype)
        return data   
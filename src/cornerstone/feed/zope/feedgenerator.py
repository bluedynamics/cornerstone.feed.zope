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

from Acquisition import Implicit
from cornerstone.feed.core.feedgenerator import FeedGenerator

class ZopeFeedGenerator(FeedGenerator, Implicit):
    
    def __init__(self, feed, name, request):
        FeedGenerator.__init__(self, feed, name)
        self.request = request
    
    def __call__(self):
        data, mimetype = self.generate()
        if mimetype is not None:
            self.request.response.setHeader('Content-Type', mimetype)
        return data
        
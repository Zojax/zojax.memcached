##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from rwproperty import getproperty, setproperty

from zope import interface, component, event
from zope.component import queryUtility, getSiteManager
from lovely.memcached.utility import MemcachedClient
from lovely.memcached.interfaces import IMemcachedClient

from interfaces import IMemcachedConfiglet, MemcachedClientUnregisterEvent


class MemcachedConfiglet(object):
    interface.implements(IMemcachedConfiglet)

    @property
    def client(self):
        client = self.data.get('memcachedClient')
        if client is None:
            client = MemcachedClient()
            self.data['memcachedClient'] = client

        return client

    def register(self):
        if queryUtility(IMemcachedClient) is not None:
            raise ValueError(
                'Memcached client already registered.')
        getSiteManager().registerUtility(self.client, IMemcachedClient)

    def unregister(self):
        event.notify(MemcachedClientUnregisterEvent())
        getSiteManager().unregisterUtility(self.client, IMemcachedClient)

    @getproperty
    def enabled(self):
        return self.data.get('enabled', False)

    @setproperty
    def enabled(self, value):
        if value:
            self.register()
        else:
            self.unregister()

        self.data['enabled'] = value


@component.adapter(IMemcachedConfiglet)
@interface.implementer(IMemcachedClient)
def memcachedClient(configlet):
    return configlet.client

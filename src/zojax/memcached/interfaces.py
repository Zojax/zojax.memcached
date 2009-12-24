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
from zope import interface, schema


class IMemcachedConfiglet(interface.Interface):
    """ memcached client configlet """

    client = interface.Attribute('IMemcachedClient object')

    enabled = schema.Bool(
        title = u'Enabled',
        description = u'Enable memcached client.',
        default = False,
        required = False)


class IMemcachedClientUnregisterEvent(interface.Interface):
    """ memcached client disabled """


class MemcachedClientUnregisterEvent(object):
    interface.implements(IMemcachedClientUnregisterEvent)

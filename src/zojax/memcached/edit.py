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
from zope import interface
from zope.app.pagetemplate import ViewPageTemplateFile
from lovely.memcached.interfaces import IMemcachedClient

from zojax.layoutform import Fields
from zojax.wizard.step import WizardStep, WizardStepForm
from zojax.wizard.interfaces import ISaveable
from zojax.widget.list import ListFieldWidget
from zojax.memcached.interfaces import IMemcachedConfiglet


class EditConfigletForm(WizardStepForm):
    interface.implements(ISaveable)

    fields = Fields(IMemcachedConfiglet, IMemcachedClient)
    fields['servers'].widgetFactory = ListFieldWidget

    @property
    def label(self):
        return self.context.__title__

    @property
    def description(self):
        return self.context.__description__


class Stats(WizardStep):

    template = ViewPageTemplateFile('stats.pt')

    def update(self):
        stats = self.context.client.getStatistics()

        if stats:
            self.rows = sorted(stats[0][1].keys())
            self.colNames = map(lambda x: x[0], stats)
            self.colData = map(lambda x: x[1], stats)

        self.stats = stats

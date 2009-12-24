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
"""Setup for zojax.memcached package

$Id$
"""
import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='0.2.0dev'


setup(name = 'zojax.memcached',
      version = version,
      author = 'Nikolay Kim',
      author_email = 'fafhrd91@gmail.com',
      description = "Memcached configuration configlet for zojax",
      long_description = (
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('CHANGES.txt')
          ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      url='http://zojax.net/',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zojax'],
      install_requires = ['setuptools', 'rwproperty',
                          'zope.component',
                          'zope.interface',
                          'zope.app.component',
                          'zojax.layout',
                          'zojax.layoutform',
                          'zojax.controlpanel',
                          'zojax.statusmessage',
                          'zojax.widget.list',
                          'zojax.wizard',
                          'lovely.memcached',
                          ],
      extras_require = dict(test=['zojax.autoinclude',
                                  'zojax.controlpanel [test]']),
      include_package_data = True,
      zip_safe = False
      )

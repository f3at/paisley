#!/usr/bin/env python
# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4

# Copyright (c) 2007-2008
# See LICENSE for details.

from setuptools import setup, find_packages


setup(name="paisley",
      version="0.3.1-feat.1",
      description=("Paisley is a CouchDB client written in Python to be used "
                   "within a Twisted application."),
      author="Paisley Developers",
      author_email="",
      license="MIT",
      platforms=['any'],
      url="http://github.com/f3at/paisley",
      download_url="http://github.com/f3at/paisley/zipball/v0.3.1-1",
      packages=find_packages(),
      include_package_data = True
    )

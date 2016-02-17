#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from setuptools import setup, find_packages
from io import open

PROJECT_MODULE = 'django_demo'
PROJECT = 'django-demo'
AUTHOR = 'Bryce Eggleton'
EMAIL = 'eggleton.bryce@gmail.com'
DESC = 'Django web framework demo application'
URL = 'https://github.com/neuroticnerd/django-demo-app'
REQUIRES = []
LONG_DESC = ''
LICENSE = ''
VERSION = '0.1.0'

with open('requirements.txt', 'r', encoding='utf-8') as requirements:
    REQUIRES = (req.strip() for req in requirements)

with open('LICENSE', 'r', encoding='utf-8') as f:
    LICENSE = f.read()

setup(
    name=PROJECT,
    version=VERSION,
    packages=find_packages(include=[PROJECT_MODULE]),
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    description=DESC,
    long_description=LONG_DESC,
    license=LICENSE,
    install_requires=REQUIRES,
)

#!/usr/bin/env python

import os
from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.md'))
long_description = f.read().strip()
f.close()


setup(
    name='drf-microservice',
    version='0.5.1',
    author='Alain IVARS',
    author_email='alainivars@gmail.com',
    url='http://github.com/alainivars/drf-microservice',
    description='''
    Create a REST API endpoints with Authentication and Registration
    ''',
    packages=find_packages(),
    long_description=long_description,
    keywords='''
    django rest auth registration rest-framework django-registration api
    ''',
    zip_safe=False,
    test_suite='setuptest.setuptest.SetupTestSuite',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

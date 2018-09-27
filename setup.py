#!/usr/bin/env python

import os
from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read().strip()

setup(
    name='drf-microservice',
    version='0.5.2',
    author='Alain IVARS',
    author_email='alainivars@gmail.com',
    url='http://github.com/alainivars/drf-microservice',
    license='Apache License 2.0',
    description='''
    Create a REST API endpoints with Authentication and Registration
    ''',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='''
    django rest auth registration rest-framework django-registration api
    ''',
    zip_safe=False,
    test_suite='setuptest.setuptest.SetupTestSuite',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: Apache License 2.0',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

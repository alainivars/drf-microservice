#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from docs.version import __version__

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read().strip()

setup(
    name='drf-microservice',
    version=__version__,
    author='Alain IVARS',
    author_email='alainivars@gmail.com',
    url='http://github.com/alainivars/drf-microservice',
    license='Apache License 2.0',
    description='''
    A REST API endpoints with Authentication and Registration.
    Read the README.rst for more information.
    ''',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords='''
    django rest auth registration rest-framework django-registration api docker cookiecuter tox pytest
    ''',
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.6.*, !=3.7.*, !=3.8.*",
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP'
    ],
)

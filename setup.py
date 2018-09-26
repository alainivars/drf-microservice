#!/usr/bin/env python

import os
from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.md'))
long_description = f.read().strip()
f.close()


setup(
    name='drf-microservice',
    version='0.5.0',
    author='Alain IVARS',
    url='http://github.com/alainivars/drf-microservice',
    description='Create a set of REST API endpoints with Authentication and Registration',
    packages=find_packages(),
    long_description=long_description,
    keywords='django rest auth registration rest-framework django-registration api',
    zip_safe=False,
    install_requires=[
        'atomicwrites==1.2.1',
        'attrs==18.2.0',
        'boto3==1.9.10',
        'botocore==1.12.10',
        'certifi==2018.8.24',
        'chardet==3.0.4',
        'click==6.7',
        'coreschema==0.0.4',
        'Django==2.1.1',
        'django-rest-auth==0.9.3',
        'django-rest-authtoken==1.2.0',
        'djangorestframework==3.8.2',
        'django-setuptest==0.2.1',
        'docutils==0.14',
        'idna==2.7',
        'itypes==1.1.0',
        'Jinja2==2.10',
        'jmespath==0.9.3',
        'MarkupSafe==1.0',
        'more-itertools==4.3.0',
        'pluggy==0.7.1',
        'py==1.6.0',
        'python-dateutil==2.7.3',
        'pytz==2018.5',
        'requests==2.19.1',
        's3transfer==0.1.13',
        'six==1.11.0',
        'uritemplate==3.0.0',
        'urllib3==1.23',
    ],
    extras_require={
        'development': [
            "coreapi==2.3.3",
            "pygments==2.2.0",
        ],
        'tests': [
            "pytest==3.8.1",
            "pytest-django==3.4.3",
            'coverage',
            'pep8',
            # 'responses>=0.5.0',
            # 'django-allauth>=0.25.0',
            # 'djangorestframework-jwt>=1.9.0',
        ],
    },
    tests_require=(
        'django-setuptest',
        "pytest==3.8.1",
        "pytest-django==3.4.3",
        'coverage',
        'pep8',
    ),
    test_suite='setuptest.setuptest.SetupTestSuite',
    include_package_data=True,
    classifiers=[
        'Framework :: Django Rest',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
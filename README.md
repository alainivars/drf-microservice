[![Build Status](https://travis-ci.org/alainivars/drf-microservice.png?branch=master)](https://travis-ci.org/alainivars/drf-microservice)
[![PyPI version](https://badge.fury.io/py/drf-microservice.svg)](https://badge.fury.io/py/drf-microservice)
[![Documentation Status](https://readthedocs.org/projects/alpha-vantage/badge/?version=latest)](http://alpha-vantage.readthedocs.io/en/latest/?badge=latest)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/alainivars/drf-microservice.svg)](http://isitmaintained.com/project/alainivars/drf-microservice "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/alainivars/drf-microservice.svg)](http://isitmaintained.com/project/alainivars/drf-microservice "Percentage of issues still open")
[![Test coverage status](https://coveralls.io/r/alainivars/drf-microservice?branch=master)](https://coveralls.io/repos/alainivars/drf-microservice/badge.svg?branch=master)
[![Requirements Status](https://requires.io/github/alainivars/drf-microservice/requirements.svg?branch=master)](https://requires.io/github/alainivars/drf-microservice/requirements/?branch=master)
[![pypi download](https://img.shields.io/pypi/dm/drf-microservice.svg)](https://pypi.python.org/pypi/drf-microservice/)
[![python supported](https://img.shields.io/pypi/pyversions/drf-microservice.svg)](https://pypi.python.org/pypi/drf-microservice/)
[![licence](https://img.shields.io/pypi/l/drf-microservice.svg)](https://pypi.python.org/pypi/drf-microservice/)
[![PyPi version](https://img.shields.io/pypi/v//drf-microservice.svg)](https://pypi.python.org/pypi/drf-microservice)
[![Code Health](https://landscape.io/github/alainivars/drf-microservice/master/landscape.svg?style=flat)](https://landscape.io/github/alainivars/drf-microservice/master)
[![Documentation status](https://readthedocs.org/projects/drf-microservice/badge/?version=latest)](https://readthedocs.org/projects/drf-microservice/?badge=latest)
[![PyPi wheel](https://pypip.in/wheel/drf-microservice/badge.svg)](https://pypi.python.org/pypi/drf-microservice/)


# drf-microservice
A POC of a DRF microservice

!!!DON"T USE IT IN PRODUCTION, It's in development!!!

Something disturb you in the code? Don't hesitate to submit a pull request and contribute.


### AWS secret required
```shell
APPNAME_USERNAME_PASSWD => a client API password
SECRET_KEY => the secret key
```
### ENV required
```shell
AWS_REGION_NAME => default="eu-east-1"
AWS_APPNAME_SECRET_NAME =>The name of the secret bucket
```
## To install
todo
```shell
git clone xxx
cd xxx
python3 -m venv /pass/to/venev
source /pass/to/venev/bin/activate
python setup.py test
python manage.py migrate
SECRET_KEY=xxx python manage.py test
```


## API
To see the documentation for the API
In development mode, login at
```web
http://127.0.0.1:8000/rest-auth/login/
```
Actually the default mode is "development" (same to the state of this project)
in that mode a default login is the the db with username='admin' password='admin'
you will get back in return your token.
 
Then open 
```web
http://127.0.0.1:8000/docs/
```
## testing
You can run the tests by:
```shell
SECRET_KEY=xxx python manage.py test
```
or by
```shell
python setup.py test
```
or by
```shell
DJANGO_SETTINGS_MODULE=project.settings SECRET_KEY=xxx pytest
```

## Security check
Before dockerization for deployment to production, don't forget to check if by
```shell
SECRET_KEY="MySecret" python manage.py check --deploy 
```
### Build and run the image with Docker

#### Build the Docker image:
````shell
docker build -t my-drf -f Dockerfile.drf-microservice .
docker build -t my-nginx -f Dockerfile.nginx .
````
#### Run the container:
````shell
docker network create my-network
docker run -d --name drf --net my-network -v /app my-drf
docker run -d --name nginx --net my-network -p "5000:80" my-nginx
````
If you want to change the port binding, it's here...


### Build and run wit docker-compose
```shell
docker-compose up
```

### DONE
    - support basic auth
    - support token auth
    - endpoint json file POST,GET
    - endpoint login/logout
    - endpoint get tocken

### TODO
    - AWS ssm secret
    - add getSentry support
    - endpoint json file DELETE,PUT?
    - add some strong auth
    - create differents version:
        - S3
        - RDS
        - postgreSQL
        - Redis
        - Aerospike
        - ... 

#### for different use-case
    - create the docker-image file
    - create the ansible file
    - create the terraform file
    - create the kubertes file
    - create the Juju file


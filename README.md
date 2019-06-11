[![Build Status](https://travis-ci.org/alainivars/drf-microservice.png?branch=master)](https://travis-ci.org/alainivars/drf-microservice)
[![PyPI version](https://badge.fury.io/py/drf-microservice.svg)](https://badge.fury.io/py/drf-microservice)
[![Documentation Status](https://readthedocs.org/projects/drf-microservice/badge/?version=latest)](http://alpha-vantage.readthedocs.io/en/latest/?badge=latest)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/alainivars/drf-microservice.svg)](http://isitmaintained.com/project/alainivars/drf-microservice "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/alainivars/drf-microservice.svg)](http://isitmaintained.com/project/alainivars/drf-microservice "Percentage of issues still open")
[![Coverage Status](https://coveralls.io/repos/github/alainivars/drf-microservice/badge.svg?branch=master)](https://coveralls.io/github/alainivars/drf-microservice?branch=master)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPi wheel](https://pypip.in/wheel/drf-microservice/badge.svg)](https://pypi.python.org/pypi/drf-microservice/)


# drf-microservice
A DRF microservice

Something disturb you in the code? Don't hesitate to submit a pull request and contribute.

### Releases Notes

    - 0.6.0: total refactoring for add cookiecutter 
    - 0.5.2: fix depencies security alert
    - 0.5.1: fix some document presentation on github and pypi
    - 0.5.0: Initial publication version

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
```
- for bash, zsh
```shell
source /pass/to/venev/bin/activate
```
- for fish
```shell
source /pass/to/venev/bin/activate.fish
```
python setup.py test
python manage.py migrate
```
- for bash, zsh
```shell
SECRET_KEY=my_secret_key python manage.py test
```
- for fish
```shell
env SECRET_KEY=my_secret_key python manage.py createsuperuser
```
- then run it
```shell
SECRET_KEY=my_secret_key python manage.py runserver
```
- if you have any proble or you want enable the debug mode
```shell
ENABLE_DEBUG=1
```


## API
To see the documentation for the API
In development mode, login at
```shell
curl --request POST \
  --url http://127.0.0.1:8000/rest-auth/login/ \
  --header 'authorization: Basic YWRtaW46YWRtaW4=' \
  --header 'content-type: application/json' \
}'
```
Actually the default mode is "development" (same to the state of this project)
in that mode a default login is the the db with username='admin' password='admin'
you will get back in return your token.
 
Then open 
```web
http://127.0.0.1:8000/docs/
```
## Testing
You can run the tests by:
```shell
SECRET_KEY=my_secret_key python manage.py test
```
or by
```shell
python setup.py test
```
or by
```shell
DJANGO_SETTINGS_MODULE={{cookiecutter.app_name}}.config.local SECRET_KEY=my_secret_key pytest
```

## Security check
Before dockerization for deployment to production, don't forget to check if by
```shell
SECRET_KEY=my_secret_key python manage.py check --deploy 
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

### Functionalities DONE
    - support basic auth
    - support token auth
    - endpoint json file POST,GET
    - endpoint login/logout
    - endpoint get tocken
    - postgreSQL support

### DevOps tools DONE
    - the docker-image file
    - the docker-compose file
    - endpoint get status Icinga2

#### Functionalities TODO
    - AWS ssm secret
    - endpoint json file DELETE,PUT?
    - create differents version:
        - Aws S3 support (in progress)
        - Aws RDS support
        - Aws Elastisearch support
        - Redis support
        - Aerospike support
        - ... 

#### DevOps tools TODO
    - the terraform file AWS (in progress)
    - the terraform file GCD
    - the terraform file Azure
    - add getSentry support
    - add Aws Cloudwatch support
    - the ansible file AWS
    - the ansible file GCD
    - the ansible file Azure
    - the Juju file AWS
    - the Juju file GCD
    - the Juju file Azure


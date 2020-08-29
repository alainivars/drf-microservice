# Load the common settings that we will overwrite as needed in our user1 settings file.
# check https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
from my_api.settings.common import *

# For example:
# ALLOWED_HOSTS = ['fathomless-scrubland-30645.herokuapp.com', '127.0.0.1']
ALLOWED_HOSTS.extend(['127.0.0.1'])

# Load the production settings that we will overwrite as needed in our user1 settings file.
from my_api.settings.common import *

ALLOWED_HOSTS.extend(['127.0.0.1', 'localhost', '0.0.0.0'])
DEBUG_URL = 1

"""
Django production settings for emailapi project.

* Inherits from base settings.
* Configures settings specific to production environment.
"""

from .base import *
from pathlib import Path
from dotenv import dotenv_values


# Load environment variables from .env file
env_vars = dotenv_values('.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_vars.get('PROD_SECRET_KEY')
ALLOWED_HOSTS = env_vars.get('PROD_ALLOWED_HOSTS')

# Debug and static content serving disabled
DEBUG = False
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Configure static root for production

# Database (replace with your production database details)
DATABASES['default']['ENGINE'] = 'django'

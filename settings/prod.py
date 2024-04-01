"""
Django production settings for emailapi project.

* Inherits from base settings.
* Configures settings specific to production environment.
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('PROD_SECRET_KEY')
ALLOWED_HOSTS = env.list('PROD_ALLOWED_HOSTS')

# Debug and static content serving disabled
DEBUG = False
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Configure static root for production

# Database (replace with your production database details)
DATABASES['default']['ENGINE'] = 'django

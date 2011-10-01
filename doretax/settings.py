# Django settings for doretax project.

import os
import sys
DEBUG = True
IS_DEV = True
TEMPLATE_DEBUG = DEBUG

# root directories
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected-static/')
# urls
MEDIA_URL = '/site_media/media/'
STATIC_URL = '/site_media/static/'
AJAX_URL = '/get/'
AJAX_VIEW_PREFIX = AJAX_URL[1:]

ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'admin/')
sys.path.append(PROJECT_ROOT)
 
ADMINS = (
    ('Cole Wiley', 'cole@decode72.com'),
    ('Zack Dever', 'zack@decode72.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'doretax.sqlite'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xx6ew5*1z2b@$9t1jx*h2qlss9t85pvsq7ce=!#z)ugc)n&t4j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'doretax.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
    os.path.join(PROJECT_ROOT, 'templates/admin/'),
    os.path.join(PROJECT_ROOT, 'templates/registration/'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static/'),
)

INSTALLED_APPS = (
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    # everything above needed for admin
    'django.contrib.localflavor',
    'django.contrib.staticfiles',
    'biz',
#    'south',
)

try:
    from local_settings import *
except ImportError:
    pass


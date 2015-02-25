"""
Django settings for zen_lunch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from socket import gethostname

DEPLOYED=False

#TODO -- get servers @zendesk
#if gethostname() in ("lunchbox01", "lunchbox02", "lunchbox"):
    DEPLOYED=True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

#TODO FIXME
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5-+pj6l27bnvzsvi0eey=sy#csh)28h1h=ws9@=sp-40psz#g8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not DEPLOYED

TEMPLATE_DEBUG = not DEPLOYED

#TODO FIXME
ALLOWED_HOSTS = [".corp.dropbox.com", "lunchbox01", "lunchbox"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'lunchboxapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#FIXME
ROOT_URLCONF = 'lunchboxproj.urls'
#FIXME
WSGI_APPLICATION = 'lunchboxproj.wsgi.application'

#FIXME
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lunchbox.db',
    }
}
#FIXME
if DEPLOYED:
    # TODO: use SSL and stop using a password
    DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.mysql',
            'HOST' : 'lunchboxdb01.corp.dropbox.com',
            'OPTIONS': {
                'read_default_file': '/home/lunchbox/secrets.cnf',
                'init_command': 'SET storage_engine=INNODB',
            },
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),
                    '/var/www/static/',
                   )
"""
Django settings for Vehiculos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c)_6aqo_z6maadij4-#-h2w%t)hxszx8trwqi$k$a%$951_y1v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Logeo
from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('index')
LOGIN_REDIRECT_URL = reverse_lazy('zonaprivada')
LOGOUT_URL = reverse_lazy('logout')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zonapublica',
    'zonaprivada',
    'braces',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Vehiculos.urls'

WSGI_APPLICATION = 'Vehiculos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
   #  'default': {
   #          'ENGINE': 'django.db.backends.postgresql_psycopg2', # Agregar la DB  'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
   #          'NAME': 'mydb',   # Agregar el nombre de la DB
   #          'USER': 'auto',   # Agregar el usaurio
   #          'PASSWORD': '123', # Agregar la contraseña
   #          'HOST': 'localhost', # Agregar el host donde esta la DB, si se encuenta local colocar localhost o '127.0.0.1'
   #          'PORT': '',          # Agregar el puerto de la DB
   # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Template location
TEMPLATE_DIRS = (
    os.path.join((BASE_DIR), "templates"),
)

# import os
# STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['static'])

# from os.path import join
# TEMPLATE_DIRS = (
#     join(BASE_DIR,  'templates'),
# )
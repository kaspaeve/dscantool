"""
Django settings for dscantool project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DSCAN_SECRET_KEY', '&f8lk5k-b$^)-sdfij8gu9df7g9aa2zagdfh8iooijioukhrs_')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('DSCAN_ALLOWED_HOST', 'dscan.nimos.ws')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dscan',
    'dscantool',
    'esi'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dscantool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dscantool.preprocessors.template_settings',
                'dscan.preprocessors.template_stats'
            ],
        },
    },
]

WSGI_APPLICATION = 'dscantool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DSCAN_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DSCAN_DB_NAME', 'dscantool'),
        'USER': os.environ.get('DSCAN_DB_USER', 'dscantool'),
        'PASSWORD': os.environ.get('DSCAN_DB_PASSWORD', 'dscantool'),
        'HOST': os.environ.get('DSCAN_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DSCAN_DB_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = os.environ.get('DSCAN_LANGUAGE_CODE', 'en-us')

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = os.environ.get('DSCAN_STATIC_URL', '/static/')
  
STATIC_ROOT = os.environ.get('DSCAN_STATIC_ROOT', '/dscantool/static/');

# Categories to sort DScans
DSCAN_CATEGORIES = {
    "Capitals": {
        "categories": [],
        "groups": [883, 485, 547, 1538, 30, 659]
    },
    "Structures": {
        "categories": [22, 23, 46, 65, 15, 16, 40],
        "groups": []
    },
    "Misc.": {
        "categories": [2, 8, 3, 18, 87, 11],
        "groups": []
    }
}

CATEGORY_ORDER = ["Capitals", "Ships", "Structures", "Misc."]

# 6 - Sun
# 7 - Planet
# 8 - Moon
# 9 - Asteroid Belt
# 15 - Station
# 1025 - Poco
# 1404 - Engineering Complex
# 1406 - Refinery
# 1657 - Citadels
SOLAR_SYSTEM_IDENTIFIERS = [6, 7, 8, 9, 15, 1657, 1404, 1406, 1025]

ESI_BASE = 'https://esi.evetech.net/latest'

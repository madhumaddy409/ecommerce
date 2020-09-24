"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


import dj_database_url

import dj_database_url
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import django_heroku

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f7hh914(mtf8-a2rc_r8sh92^7i$qm!29v)-r88cpv47#5n@)='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'cart',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',



]

ROOT_URLCONF = 'ecommerce.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases



DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',


        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecommerce',
        'USERNAME': 'maddy',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
        # 'NAME': 'dds6d7utnh4ut0',
        # 'USERNAME': 'pkxrmlruugazzy',
        # 'PASSWORD': '970cc9fddf2a7867d56f9c6851fe904974a72e30f06d350893e24afd13469b6c',
        # 'HOST': 'ec2-54-160-202-3.compute-1.amazonaws.com',
        # 'PORT': '5432',
    }
}


# POSTGRES_URL = "postgres://pkxrmlruugazzy:970cc9fddf2a7867d56f9c6851fe904974a72e30f06d350893e24afd13469b6c@ec2-54-160-202-3.compute-1.amazonaws.com:5432/dds6d7utnh4ut0"
# DATABASES = {'default': dj_database_url.config(default=os.environ[POSTGRES_URL])}
#
# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': dj_database_url.config(default='postgres://maddy:root@localhost:5432/ecommerce')
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')






REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "/media/"
from .base import *
from os import getenv

DEBUG = True

ALLOWED_HOSTS = ["localhost"]

DATABASES = {
    'default': {
        'ENGINE': getenv('DB_ENGINE'),
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
        'HOST': getenv('DB_HOST'),
        'PORT': getenv('DB_PORT'),
    }
}

WSGI_APPLICATION = "passwordSafe.wsgi.application"


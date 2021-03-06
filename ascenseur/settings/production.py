# -*- coding: utf-8 -*-

from .base import *

import os


# POUR LIRE LES CLES A PARTIR DU FICHIER JSON NON ENREGISTRE DANS GIT
import json
from django.core.exceptions import ImproperlyConfigured

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, mes_Secrets = secrets):
    """Get secret setting or fail with ImproperlyConfigured
    """
    try:
        return mes_Secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [u'www.ascenseur-en-copropriete.com',u'www.ascenseur-en-copropriete.fr']



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yomams$ascenseur',
        'USER': 'yomams',
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': 'yomams.mysql.pythonanywhere-services.com',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# endroit ou ce sera stocké sur le serveur
STATIC_ROOT = os.path.join(ENV_DIR, 'static/')
# url à laquelle elle sera servie : www.ascenseur-en-copropriete.com/static/
STATIC_URL = '/static/'
# endroit où les fichier statiques sont avant collectstatic, avant d'être dans static root
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "ascenseur/static"),
]

MEDIA_ROOT = os.path.join(ENV_DIR, 'media/')
MEDIA_URL = '/media/'
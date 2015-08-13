# -*- coding: utf-8 -*-
from default_settings import *

import os
path = os.path.abspath(os.path.dirname(__file__))


#DEBUG = True
TEMPLATE_DEBUG = DEBUG


###########################################################################
#                            database settings                            #
###########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GreenPathways',
        'USER': 'GreenPathways',
        'PASSWORD': '3378bdb53b5e0c731940',
    }
}


###########################################################################
#                             email settings                              #
###########################################################################

DEFAULT_FROM_EMAIL = 'angelo@ma-work.co.uk'

# GMail Email setup
# -----------------

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 587

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(PROJECT_ROOT, 'logs/emails/')

# SES Email setup
# ---------------

#EMAIL_BACKEND = 'django_ses.SESBackend'
#AWS_ACCESS_KEY_ID = ''
#AWS_SECRET_ACCESS_KEY = ''


###########################################################################
#                        media / static files urls                        #
###########################################################################

MEDIA_URL = 'http://media.pathways.madebyma.com/'

STATIC_URL = 'http://static.pathways.madebyma.com/'
COMPRESS_URL = STATIC_URL


###########################################################################
#                              secret sauce                               #
###########################################################################

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bxz6adg+fado-=(di077)yw)+*%vcq91(hjrs06c$=r4e4dich'

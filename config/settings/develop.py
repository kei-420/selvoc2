# import environ
from .base import *


#####################
# Security settings #
#####################

DEBUG = True

SECRET_KEY = 'ats=^uq$)6pn6ubw#hp$r3vwa36qd@0+f-c1c)kmu-jp4&u5s='
ALLOWED_HOST = ['*']


############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'selvoc_test',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'sql_mode': 'TRADITIONAL',
        }
    }
}

###########
# Logging #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'develop':{
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d ''%(message)s'
        },
    },
    'handlers': {
        'console':  {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

################
# Static files #
################

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

##################
# Email settings #
##################

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#################
# debug toolbar #
#################

if DEBUG:
    def show_toolbar(request):
        return True


    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

INTERNAL_IPS = ['127.0.0.1']





















from .base import *

SECRET_KEY = '#1!bwd-y$dmyx!hu0q&miy^*pfv!b73f6osks_9z^@x-s&h4dg'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_vuejs_local',
        'USER': 'admin_local',
        'PASSWORD': 'L0c@Ldmin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
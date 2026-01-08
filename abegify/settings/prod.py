from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INSTALLED_APPS += [
    "django_rq",
]
ALLOWED_HOSTS = env.get("ALLOWED_HOSTS", '').split(',') + ['*']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ['https://abegify.com', 'https://www.abegify.com']

STATIC_ROOT = STATIC_DIR
MEDIA_ROOT = MEDIA_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get("DATABASE_NAME"),
        'USER': env.get("DATABASE_USER"),
        'PASSWORD': env.get("DATABASE_PASSWORD"),
        'HOST': env.get("DATABASE_HOST"),
        'PORT': env.get("DATABASE_PORT"),
        'OPTIONS': {
            
        },
    }
}

TASKS = {
    "default": {
        "BACKEND": "django_tasks.backends.rq.RQBackend",
        "QUEUES": ["default", "special"],
        "OPTIONS": {
            "queues": {
                "low_priority": {
                    "max_attempts": 5,
                }
            },
            "max_attempts": 10,
            "backoff_factor": 3,
            "purge": {
                "finished": "10 days",
                "unfinished": "20 days",
            },
        },
    }
}



RQ_QUEUES = {
    "default": {
        "HOST": "redis",
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": 360,
    },
    "special": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
        "DEFAULT_TIMEOUT": 360,
    }
}

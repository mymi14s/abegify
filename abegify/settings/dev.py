from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
STATICFILES_DIRS = [
    BASE_DIR / "static", 
]

ALLOWED_HOSTS = ["*", "careful-possum-suitable.ngrok-free.app"]

INSTALLED_APPS += [
    "django_tasks.backends.database",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abegify',
        'USER': env.get("DATABASE_USER"),
        'PASSWORD': env.get("DATABASE_PASSWORD"),
        'HOST': env.get("DATABASE_HOST"),
        'PORT': env.get("DATABASE_PORT"),
        'OPTIONS': {
            "ssl_mode": "DISABLED",
        },
    }
}

CORS_ALLOW_ALL_ORIGINS = False 
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
    "https://careful-possum-suitable.ngrok-free.app",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
    "https://careful-possum-suitable.ngrok-free.app",
]

TASKS = {
    "default": {
        "BACKEND": "django_tasks.backends.database.DatabaseBackend",
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


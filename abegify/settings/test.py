from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
STATIC_ROOT = STATIC_DIR
MEDIA_ROOT = MEDIA_DIR

ALLOWED_HOSTS = ["*"]

DATABASES["default"]["OPTIONS"]["ssl_mode"] = "DISABLED"

CORS_ALLOW_ALL_ORIGINS = False 
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
]
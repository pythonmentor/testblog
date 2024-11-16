from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Configuration of Django-vite
DJANGO_VITE = {
    "default": {"dev_mode": True},
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(s$k(11!=^zzjag2m0f0th3a0b51pkz_(m^ok^&#3%5^@dd6rb"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass

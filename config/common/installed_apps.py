# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.users",
    # "apps.auth_jwt",
    "apps.cabinets",
    "apps.doctors",
    "apps.intervals",
]

INSTALLED_APPS += LOCAL_APPS
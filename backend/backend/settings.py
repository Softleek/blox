"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys
from pathlib import Path

from decouple import config

import pymysql
import json

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_PATH = BASE_DIR.parent
CONFIG_PATH = os.path.join(PROJECT_PATH, "config")
SITE_PATH = os.path.join(PROJECT_PATH, "sites")
sys.path.append(str(PROJECT_PATH)) 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-j7#rvr!*&u(2f*x28y2+m7qlgg6_dwryv%m1*a@yhp3u58qatp",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "django_filters",
    "django_crontab",
    "core",      
    'masafa_app',
]

MIDDLEWARE = [
    'core.middleware.TenantMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'core.middleware.UserActivityMiddleware', 
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


AUTH_USER_MODEL = "core.User"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["Content-Type", "Authorization", "X-Tenant"]
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
# ]


# URL configuration
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# ----------------------------------------------------------------------
# Auth and user
# ----------------------------------------------------------------------




REST_USE_JWT = True

# ----------------------------------------------------------------------
# Email settings (replace with your email configuration)
# ----------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST", default="smtp.example.com")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="user@example.com")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="password")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", default=False, cast=bool)
EMAIL_SSL_CERTFILE = config("EMAIL_SSL_CERTFILE", default=None)
EMAIL_SSL_KEYFILE = config("EMAIL_SSL_KEYFILE", default=None)
EMAIL_TIMEOUT = config("EMAIL_TIMEOUT", default=10, cast=int)
EMAIL_SSL_CAFILE = config("EMAIL_SSL_CAFILE", default=None)

SERVER_EMAIL = config("SERVER_EMAIL", default="server@example.com")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="webmaster@example.com")


# ----------------------------------------------------------------------
# Configure allauth settings
# ----------------------------------------------------------------------

ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = (
    "/"  # Redirect URL after email verification
)
ACCOUNT_EMAIL_CONFIRMATION_SIGNUP_MESSAGE = "account/confirmation_signup_message.txt"


SMS_API_KEY = config("SMS_API_KEY", default="")
SMS_CLIENT_ID = config("SMS_CLIENT_ID", default="") 
SMS_SENDER_ID = config("SMS_SENDER_ID", default="") 
SMS_API_URL = config("SMS_API_URL", default="") 
SMS_IS_UNICODE = True
SMS_IS_FLASH = True

# APPEND_SLASH = False

# Define the logs directory within the api folder
# LOGS_DIR = os.path.join(BASE_DIR, "api", "logs")

# Ensure the logs directory exists
# os.makedirs(LOGS_DIR, exist_ok=True)

CRONJOBS = [
    (
        "*/1 * * * *",
        "core.crons.send_reminder_notifications",
        f">> {os.path.join(BASE_DIR, 'core', 'logs','send_upcoming_event_notifications.log')} 2>&1",
    ),
]


# Load database configurations from sites.json
with open(os.path.join(PROJECT_PATH, 'sites', 'sites.json')) as f:
    sites = json.load(f)

# Define the default database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Add databases from sites.json
for site in sites:
    DATABASES[site['site_name']] = site['database']


DATABASE_ROUTERS = ['core.db_router.MultiTenantRouter']


sys.path.append(str(os.path.join(PROJECT_PATH, "apps", "masafa")))

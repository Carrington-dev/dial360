import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    # 'rest_framework.authtoken', # new line for token
    'rest_framework_simplejwt', #new line
    'djoser',
    'security',

   
    
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'authweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'authweb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'security.User'


CORS_ORIGIN_ALLOW_ALL = True


CORS_ALLOWED_ORIGINS = [
    "https://www.example.com",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    'http://localhost:*',
    
]

AUTH_USER_MODEL = 'security.User'

MEDIA_URL = 'media/'
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'extras/static/')
MEDIA_ROOT = os.path.join(BASE_DIR,'extras/media/')

# STATIC_ROOT = os.path.join(BASE_DIR, 'extra/static')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'extra/media')


STATICFILES_DIRS = [
    # BASE_DIR / "static",
    os.path.join(BASE_DIR,'extras/assets/')
    # "/var/www/static/",
]


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'secrets/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'secrets/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'secrets/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    # 'USERNAME_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'SERIALIZERS': {
        'user_create': 'security.serializers.UserCreateSerializer',
        'user': 'security.serializers.UserCreateSerializer',
        # 'user_create': 'djoser.serializers.UserCreateSerializer',
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    
   
}


GRAPPELLI_ADMIN_TITLE = "Oftmart Inc"

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
DEFAULT_FROM_ADMIN = config("DEFAULT_FROM_ADMIN")

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,
}
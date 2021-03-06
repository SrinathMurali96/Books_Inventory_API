import logging.config
import logging.handlers
import os
import configparser
import psycopg2.extensions

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ik2r=3^vjrb1jh9s$5g!6+2pqkfisw-#x)bmt!=_+68$n(1i2z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
	 'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CSRF_COOKIE_HTTPONLY = True

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

config = configparser.ConfigParser()
config.read('property.ini')


#WSGI_APPLICATION =  project.wsgi.application

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    # ...
    'OPTIONS': {
        'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
    },
}




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


DEFAULT_DJFORGE_REDIS_MULTITOKENS = {
    'DJFORGE_REDIS_MULTITOKENS':
        {
            'REDIS_DB_NAME': 'tokens',
            'RESET_TOKEN_TTL_ON_USER_LOG_IN': True,
            'OVERWRITE_NONE_TTL': True,
        }
}


class DRFRedisMultipleTokensrSettings:
    def __init__(self, defaults):
        self.defaults = defaults
        self.overrides = getattr(settings, 'DJFORGE_REDIS_MULTITOKENS', {})

    def __getattr__(self, item):
        try:
            return self.overrides[item]
        except KeyError:
            return self.defaults[item]


djforge_redis_multitokens_settings = DRFRedisMultipleTokensrSettings(
    DEFAULT_DJFORGE_REDIS_MULTITOKENS['DJFORGE_REDIS_MULTITOKENS']
)
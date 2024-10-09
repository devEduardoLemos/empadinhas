import os
from decouple import config
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
# import pymysql

sentry_sdk.init(
    dsn="https://94d1d72580ac4d05b0fb90c1f9c1cccd@o1084842.ingest.sentry.io/6094972",
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.1,
    send_default_pii=True
 )


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '157.245.85.137', 'app.comaempadinhas.com.br','portal.comaempadinhas.com.br']

ALLOWED_HOSTS = [
    'empadinhas-new-app-ewh3s.ondigitalocean.app',
    'app.comaempadinhas.com.br',
    'portal.comaempadinhas.com.br',  # Add other domains as necessary
]

CSRF_TRUSTED_ORIGINS = [
    'https://empadinhas-new-app-ewh3s.ondigitalocean.app',
    'https://app.comaempadinhas.com.br',
    'https://portal.comaempadinhas.com.br',  # Add other trusted origins if needed
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'widget_tweaks',
    'django_filters',
    'whitenoise.runserver_nostatic',
    'apps.usuarios',
    'apps.lojas',
    'apps.pedidos',
    'apps.entrega',
    'apps.estoque',
    'apps.inventario',
    'apps.relatorios'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projeto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'projeto/templates'),
            os.path.join(BASE_DIR, 'apps/usuarios/templates'),
            os.path.join(BASE_DIR, 'apps/pedidos/templates'),
            os.path.join(BASE_DIR, 'apps/entrega/templates'),
            os.path.join(BASE_DIR, 'apps/estoque/templates'),
            os.path.join(BASE_DIR, 'apps/inventario/templates')
        ],
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

WSGI_APPLICATION = 'projeto.wsgi.application'


DATABASES = {  
   'default': {  
       'ENGINE': 'django.db.backends.postgresql',  
       'NAME': config('DATABASE_NAME'),  
       'USER': config('DATABASE_USER'),  
       'PASSWORD': config('DATABASE_PASSWORD'),  
       'HOST': config('DATABASE_HOST'),  
       'PORT': config('DATABASE_PORT', cast=int),
       'CONN_MAX_AGE': 0,  # Let the pool handle connection reuse
        'OPTIONS': {
            'sslmode': 'require',  # Enforce SSL
        },  
   }  
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR,'db.sqlite3'),  # Path to your local SQLite database file
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  
#         'NAME': config('DATABASE_NAME'),      
#         'USER': config('DATABASE_USER'),          
#         'PASSWORD': config('DATABASE_PASSWORD'),  
#         'HOST': config('DATABASE_HOST'),                   
#         'PORT': config('DATABASE_PORT'),                      
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         }
#     }
# }

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


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = config('TIME_ZONE')
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'projeto/static')
]

LOGIN_REDIRECT_URL = '/' 
LOGIN_URL = '/login'
AUTH_USER_MODEL = 'usuarios.User'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = config('SESSION_COOKIE_AGE', cast=int)
SESSION_SAVE_EVERY_REQUEST = True

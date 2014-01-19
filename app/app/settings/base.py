import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '##%he5sc1%^9oqlf=dq8ae&k1kw(17q^)-=%f7u$rq9)_d06g_'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['django-writingfield-demo.herokuapp.com']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'writingfield',
    'gunicorn',
    'things',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'writingfield.middleware.WritingFieldMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'

STATIC_ROOT = 'srv/static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../templates/'),
)
LOGGING = {
    'version': 1,
}
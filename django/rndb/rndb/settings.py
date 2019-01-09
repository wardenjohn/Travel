"""
Django settings for rndb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uu@#+v5e5hl8hy+q!28(g!m&=)=s@$^n(lsz8z3q+hz!r2(=#5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*','192.168.1.108','10.2.102.146']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	
	'REACT',
	'newsdb',
	'userdb',
	'turenews',
	'mark',
	'diary',
	'food_information',
	'foodshop',
	'foodshop_estimate',	
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'RNDATA',
        'USER':'root',
        'PASSWORD':'11111111',
		'HOST':'127.0.0.1',
		'PORT':'3306'
    }
}

ROOT_URLCONF = 'rndb.urls'

WSGI_APPLICATION = 'rndb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'RNDATA',
		'USER':'root',
		'PASSWORD':'11111111',
		'CHARSET':'utf8',
		'HOST':'127.0.0.1',
		'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
FILE_CHARSET = 'utf-8'

DEFAULT_CHARSET = 'utf-8'

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

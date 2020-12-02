"""Base settings for Facet. Development and Production inherit from this."""


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories used in these settings files
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath(SETTINGS_DIR + "/..")
GIT_DIR = os.path.abspath(PROJECT_DIR + "/..")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0vsz0q4r@n=081oa@c49$(vq))b#2%0mp_&g)(l8&e_gutnn$a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'base.apps.BaseConfig',
    'editorial.apps.EditorialConfig',
    'entity.apps.EntityConfig',
    'participant.apps.ParticipantConfig',
    'internalasset.apps.InternalassetConfig',
    'freelance.apps.FreelanceConfig',
    'subscription.apps.SubscriptionConfig',
    'transaction.apps.TransactionConfig',
    'task.apps.TaskConfig',
    'note.apps.NoteConfig',
    'timeline.apps.TimelineConfig',
    'communication.apps.CommunicationConfig',
    'digital.apps.DigitalConfig',
    'data.apps.DataConfig',
    'engagement.apps.EngagementConfig',
    'pickup.apps.PickupConfig',
    'rollcall.apps.RollcallConfig',
    'pavilion.apps.PavilionConfig',
    'glassbreak.apps.GlassbreakConfig',
    'formation.apps.FormationConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'imagekit',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'facet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(PROJECT_DIR, 'templates')),],
        # 'DIRS': [os.path.join(PROJECT_DIR, "templates")],
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

WSGI_APPLICATION = 'facet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'multifacet',
        'HOST': 'localhost',
        'USER': 'multifacet',
        'PASSWORD': 'collab'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Email
SERVER_EMAIL = DEFAULT_FROM_EMAIL = "collaborate@projectfacet.org"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email these people when errors happen on production sites
ADMINS = [
    ('Heather', 'heather@projectfacet.org'),
]

AUTH_USER_MODEL = 'base.Participant'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
LOGIN_REDIRECT_URL = 'base:dashboard'
LOGOUT_REDIRECT_URL = 'base:dashboard'

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = GIT_DIR + "/static/"
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

MEDIA_ROOT = GIT_DIR + "/media/"
MEDIA_URL = "/media/"

######################################
# ImageKit (Django app for resizing image fields)

# Be optimistic, produce URLs for images that may not exist.
#
# This is helpful as it means we don't need to have a media file on the development/staging
# server in order to show a view that uses it. It will optimistically make the URL, hoping
# it is there. This does mean that when you add/change an ImageKit field, you need to
# regenerate the images with ``python manage.py generateimages``

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.Optimistic'

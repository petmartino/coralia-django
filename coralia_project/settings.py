import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dummy-key-for-local-dev-change-later'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'musicaparamisas.com', 'www.musicaparamisas.com', '198.58.99.196', 'new.musicaparamisas.com']

# (Keep all existing content)
# ...

INSTALLED_APPS = [
    'admin_reorder', # <-- MUST BE BEFORE 'django.contrib.admin'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # --- ADDED APP ---
    'request',
    # Our local apps
    'main.apps.MainConfig',
    'quotes.apps.QuotesConfig',
    'analytics.apps.AnalyticsConfig', # <-- UNCOMMENT THIS
    'user_visit',
    'adminsortable2',
]
# (Keep all other content the same)
# ...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # --- ADDED MIDDLEWARE ---
    'request.middleware.RequestMiddleware',
    'analytics.middleware.VisitTrackingMiddleware', # <-- UNCOMMENT THIS
    'user_visit.middleware.UserVisitMiddleware',
    # --- REORDER admin_reorder middleware
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'coralia_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'coralia_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# This is the directory where collectstatic will gather all static files
# for production deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# This is the storage engine that manages static files in production
# It's provided by the WhiteNoise package we installed.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py

# ... (at the bottom of the file)
# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # --- ADDED MIDDLEWARE ---
    'request.middleware.RequestMiddleware',
    'analytics.middleware.VisitTrackingMiddleware', # <-- UNCOMMENT THIS
    'user_visit.middleware.UserVisitMiddleware',
    # --- REORDER admin_reorder middleware
    'admin_reorder.middleware.ModelAdminReorder',
]

ADMIN_REORDER = (
    # Group all quote-related models together
    {'app': 'quotes', 'label': 'Cotizaciones y Programas',
     'models': ('quotes.Quote', 'quotes.EventType', 'quotes.Program', 'quotes.Package')
    },
    # Group main content models
    {'app': 'main', 'label': 'Contenido Principal',
     'models': ('main.RepertoirePiece', 'main.Tag')
    },
    # Group analytics models
    {'app': 'analytics', 'label': 'Estadísticas del Sitio',
     'models': ('analytics.Visit', 'request.Request')
    },
    # Keep auth models together
    {'app': 'auth', 'label': 'Autorización', 'models': ('auth.User', 'auth.Group')},
)


# NEW: This forces the reordering logic to apply on every admin page.
ADMIN_REORDER_FE_ONLY = False 


REQUEST_IGNORE_PATHS = (
    r'^admin/',
)
REQUEST_IGNORE_USER_AGENTS = (
    r'^$', # ignore requests with no user agent string set
    r'Googlebot',
    r'Baiduspider',
)
REQUEST_LOG_USER = False